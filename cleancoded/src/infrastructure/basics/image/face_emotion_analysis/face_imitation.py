import cv2
from statistics import mode
import random
from deepface import DeepFace
import rospy
from face_pkg.msg import Array2D,Array3D,Emotion,List
from sensor_msgs.msg import CameraInfo,Image
import numpy as np
import mediapipe as mp
from cv_bridge import CvBridge

mp_face_mesh = mp.solutions.face_mesh  # initialize the face mesh model
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils


'''
Face Emotion Analysis publisher node
Taking the camera input in, analyzing it, 
then publish it on the related topic through a 2D array message 
containing the list of names and the probability of the given emotion being the answer
(The higher the number, the stronger assurance)
'''
class FaceDetection():  
    cv_bridge=CvBridge()

    def __init__(self):
        self.frame_msgs = None
        self.face_cascade_name = None
        self.face_cascade = None
        self.img = None
        self.face_width = None
        self.global_dominant_emotion = []
        self.submsg = Emotion()
        self.msg = Array2D()
        rospy.init_node('FaceEmotionAnalysis',anonymous=False)
        self.pub = rospy.Publisher('/face_emotions',Array2D, queue_size=10)
        rospy.Subscriber('/image_cv2',List,self.catch)

        rospy.Subscriber("/camera_info", CameraInfo, self.syncinfo, queue_size=10)

        while not rospy.is_shutdown():
             rospy.spin()
    
    def syncinfo(self, info):  # sync camera video stream info
        self.height = info.height
        self.width = info.width
        
    def prequisites(self,image):
        with mp_holistic.Holistic(
        # max_num_faces=1,  # number of faces to track in each frame
        refine_face_landmarks=True,  # includes iris landmarks in the face mesh model
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
        
            
            image = cv2.resize(image, (800, 600))
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # frame to RGB for the face-mesh model
            results = face_mesh.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # frame back to BGR for OpenCV
            while not results.face_landmarks:
                print("No face detected")
            else: 
                print("Nobody is headless thanks god!")
                self.frame_msgs = image
                self.face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  #getting a haarcascade xml file
                self.face_cascade = cv2.CascadeClassifier()  #processing it for our project
                if not self.face_cascade.load(cv2.samples.findFile(self.face_cascade_name)):  #adding a fallback event
                    print("Error loading xml file")
                gray = cv2.cvtColor(self.frame_msgs, cv2.COLOR_BGR2GRAY)
                face=self.face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
                
                for x,y,w,h in face:
                        self.img=cv2.rectangle(self.frame_msgs,(x,y),(x+w,y+h),
                        (random.randint(0,255),random.randint(0,255),random.randint(0,255)),1)  #making a recentangle to show up and detect the face and setting it position and colour
                        self.face_width = h
            

    def analysis(self,image):
            self.prequisites(image)
            analyze = DeepFace.analyze(self.frame_msgs,actions=['emotion'], enforce_detection=False)  #same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
            result = [analyze]
            
            return result

    def catch(self,_):
        arr = []
        l = _.list
        for i in range(len(l)):
            arr.append(list(l[i].data))
        # sub.unregister()
        self.arrrrr= np.array(arr, dtype=np.uint8).reshape((640,480,3))
        self.feedback(self.arrrrr)

    def convert_back(self):
        frame_in_ros = self.cv_bridge.cv2_to_imgmsg(self.arrrrr)
        frame_in_ros.encoding = "rgb8"
        msg = Image()
        msg = frame_in_ros
        cv2.imwrite('testaki.jpg',self.arrrrr)
        return msg


    def feedback(self,image):  
        image = cv2.resize(image,(self.height,self.width))
        feedback = self.analysis(image)
        emotion = feedback[0]['emotion']
        dominant = feedback[0]['dominant_emotion']

        if len(self.global_dominant_emotion) <= 50:
            self.global_dominant_emotion.append(str(dominant))
        else:
            self.global_dominant_emotion = []
            self.global_dominant_emotion.append(str(dominant))

        overall_emotion = mode(self.global_dominant_emotion)
        # Sorting emotions by higher propablity values gotten
        sorted_values = sorted(emotion.items(), key=lambda item: item[1])[::-1]
        prettied_dict = [str(i)+' : '+str(round(j,6)) for i,j in sorted_values]+['Dominant Emotion : '+str(overall_emotion)]
        temp = []

        for item in sorted_values:
            self.submsg = Emotion()
            self.submsg.name, self.submsg.probability = item[0], float(round(item[1],6))
            temp.append(self.submsg)
            print(temp)
        self.msg.list = temp
        self.pub.publish(self.msg)
        self.msg.list = []
        # rospy.Rate(5).sleep()
        # Converting to string to display on the camera frame output
        prettied_str = '\n'.join(prettied_dict)
        return prettied_str
    


if __name__ == '__main__':
    FaceDetection()