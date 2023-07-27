import os
import sys
import time
from statistics import mode

import cv2
import pandas as pd
import Emotion_estimation.face_imitation as emo
import mediapipe as mp
import Pose_estimation.pose as ps
import write_to_file as wf
from Gaze_estimation.gaze import GazePosition, GazeTracking, HeadPosition
from Pose_estimation.matrix import draw_grid as gd
from Pose_estimation.matrix import gridding as gdplt
import pyflowchart as pfc
import glob2 as glob

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = os.path.dirname(os.path.abspath(__file__)) + '\\**\\*.py'

for i in glob.glob(p,recursive=True):
    # print([i if '.py' in i else ''])
    if '.py' in i:
        try:
            with open(i) as f:
                code = f.read()
                flowchart = pfc.Flowchart.from_code(code, inner=True, simplify=True)
                with open('file.txt','a') as fs:
                    fs.write(flowchart.flowchart())
            
            print(flowchart.flowchart())
        except: pass

mp_face_mesh = mp.solutions.face_mesh  # initialize the face mesh model
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

gaze = GazeTracking()
dominant_emotion = emo.FaceDetection()  
# camera stream:
previousTime = 0
currentTime = 0
datafile = wf.DataClassify('face params.xlsx')
cap = cv2.VideoCapture(0)  # chose camera index (try 1, 2, 3)
# cap = cv2.VideoCapture("C:\\Users\\Mahta\\Documents\\GitHub\\autism_Robot\\src\\face_pkg\\scripts\\detections\\video.mp4")  # chose camera index (try 1, 2, 3)
count = 0
gap = False

headers = [
    'dominant emotion: %',
    'mean emotion after 50 rounds',
    'emotion scores',
    'gaze pos',
    'head pos',
    'head tilt',
    'elapsed time'
]
# اینا رو همشون با این هدرا توی مسیج های روبات بفرستیم. یه مسیج جدید تعریف کنم که اینا رو به علاوه زمان شامل بشه که منظم بشه دریافتشون کرد به ازای هر دسته فریم.
def add_list_to_frame(data,y0,dy=25,dtype="list",color="(255,255,255)"): # The function to enumerate through multiple objects to write in lines on the frame
    for i,item in enumerate(data):
        y = y0 + i*dy
        if dtype == 'dict':
            line = item[0]+':'+str(item[1])
        else: line = item
        cv2.putText(image, line, (10, y), cv2.FONT_HERSHEY_COMPLEX, 0.45, color, 1)
    return y + dy


with mp_holistic.Holistic(
        # max_num_faces=1,  # number of faces to track in each frame
        refine_face_landmarks=True,  # includes iris landmarks in the face mesh model
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
        
    columns = []
    data_table = []
    while cap.isOpened():
        success, image = cap.read()
        cap.set(cv2.CAP_PROP_POS_FRAMES, count) #set new frame to 'count'th frame

        if not success:  # no frame input
            print("Ignoring empty camera frame.")
            time.sleep(3)
            break

        
        count += 10 # Skipping 30 frames per second to slow the processes a little
        image = cv2.resize(image, (800, 600))
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # frame to RGB for the face-mesh model
        results = face_mesh.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # frame back to BGR for OpenCV

        # Initializing current time and precious time for calculating the FPS
        currentTime = str((time.perf_counter()/60).__round__())+':'+str((time.perf_counter()%60).__round__()) # time in seconds
        fps = cv2.CAP_PROP_POS_FRAMES
        # previousTime = currentTime - previousTime
        
    

        if results.face_landmarks:
            if gap: #controlling pause for recallibration after face not being detected 
                time.sleep(3)
                gap = False
                
            ps.MeshDetector(image, mp_holistic, results)
            gazedir = GazePosition(image, results.face_landmarks).__str__()  # gaze estimation
            gaze_pos = gazedir[0]
            pupil_dir = gazedir[1]
            head_pos = HeadPosition(image, results.face_landmarks).__str__()
            emotions = dominant_emotion.__str__(image)
            dominant_emo = mode(dominant_emotion.global_dominant_emotion)
			# Displaying FPS on the image
            cv2.putText(image, str(currentTime)+" Elapsed time", (10, 550), cv2.FONT_HERSHEY_COMPLEX, 0.45, (255,0,0), 1)
            # Displaying Gaze Position on the image
            cv2.putText(image, 'looking at '+gaze_pos, (10, 40), cv2.FONT_HERSHEY_COMPLEX, 0.65, (0,255,0), 1)


            y = add_list_to_frame(data=emotions.split('\n'), y0=80, dy=25, color=(255,255,255))
            y = add_list_to_frame(data=head_pos[1].items(), dtype='dict',y0=y, dy=25, color=(255,255,128))

            data_table += [[emotions.split('\n')[0],dominant_emo,emotions.split('\n'),pupil_dir,head_pos[0][5:],head_pos[1],currentTime]]
            columns += [count]
            if count%200 == 0: #backup temp data to prevent data loss
                datafile.sheet(data_table, headers=headers,columns=columns, sheet_name='temp%s'%str(count))
            
        else:
            gap = True
            cv2.putText(image, 'No face detected. Waiting...', (10, 550), cv2.FONT_HERSHEY_COMPLEX, 0.45, (255,0,0), 1)
            data_table.append(['No face detected','-','-','-','-','-',currentTime])
            print('No face detected. Waiting...')


        cv2.imshow('output window', image)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cap.release()
print('Saving data...')
#sending the data to be written in a file
datafile.sheet(data_table, headers=headers,columns=columns,if_sheet_exists='new')
print('Saved. Quiting')

