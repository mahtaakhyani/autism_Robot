import os, sys
import time
import mediapipe as mp
import cv2
from Gaze_estimation.gaze import GazeTracking, GazePosition
import Pose_estimation.pose as ps
import Emotion_estimation.face_imitation as emo

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



mp_face_mesh = mp.solutions.face_mesh  # initialize the face mesh model
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils


gaze = GazeTracking()
dominant_emotion = emo.FaceDetection()  
# camera stream:
previousTime = 0
currentTime = 0
cap = cv2.VideoCapture(0)  # chose camera index (try 1, 2, 3)
count = 0
with mp_holistic.Holistic(
        # max_num_faces=1,  # number of faces to track in each frame
        refine_face_landmarks=True,  # includes iris landmarks in the face mesh model
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
        
    while cap.isOpened():
        success, image = cap.read()
        cap.set(cv2.CAP_PROP_POS_FRAMES, count) #set new frame to 'count'th frame

        if not success:  # no frame input
            print("Ignoring empty camera frame.")
            continue
        
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
            ps.MeshDetector(image, mp_holistic, results)
            gaze_pos = GazePosition(image, results.face_landmarks).__str__()  # gaze estimation
            emotions = dominant_emotion.__str__(image)
            # write the outputed pose to the image frame
            # Calculating the FPS
			# Displaying FPS on the image
            cv2.putText(image, str(currentTime)+" Elapsed time", (10, 550), cv2.FONT_HERSHEY_COMPLEX, 0.45, (255,0,0), 1)
            # Displaying Gaze Position on the image
            cv2.putText(image, 'looking at '+gaze_pos, (10, 40), cv2.FONT_HERSHEY_COMPLEX, 0.65, (0,255,0), 1)

            dy = 25
            y0 = 80
            for i, line in enumerate(emotions.split('\n')):
                y = y0 + i*dy
                cv2.putText(image, line, (10, y), cv2.FONT_HERSHEY_COMPLEX, 0.45, (255,255,255), 1)

        cv2.imshow('output window', image)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cap.release()
