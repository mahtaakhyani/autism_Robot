
import cv2
from cv_bridge import CvBridge
from deepface import DeepFace
# from face_pkg.msg import Exp
# from sensor_msgs import Image


class FaceDetection():  
    def __init__(self,frame):
        self.frame_msgs = frame
        self.cv_bridge = CvBridge()
        # rospy.init_node('webcam', anonymous=False)
        # self.img_pub = rospy.Publisher('/webcam/image', Image, queue_size=10 )
        # rospy.Subscriber('/camera/image_raw', Image , self.main)
        self.face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  #getting a haarcascade xml file
        self.face_cascade = cv2.CascadeClassifier()  #processing it for our project
        if not self.face_cascade.load(cv2.samples.findFile(self.face_cascade_name)):  #adding a fallback event
            print("Error loading xml file")



    def main(self):
        self.video=cv2.VideoCapture(0)  #requesting the input from the webcam or camera

        while cv2.VideoCapture(0).isOpened():  #checking if are getting video feed and using it
            self.frame_in_cv2 = self.cv_bridge.imgmsg_to_cv2(
            self.frame_msgs, desired_encoding='passthrough')
            # Transform to grayscale,
            # available encodings: http://docs.ros.org/jade/api/sensor_msgs/html/image__encodings_8h_source.html
            if "rgb" in self.frame_msgs.encoding:
                gray = cv2.cvtColor(self.frame_in_cv2, cv2.COLOR_RGB2GRAY)
            elif "bgr" in self.frame_msgs.encoding:
                gray = cv2.cvtColor(self.frame_in_cv2, cv2.COLOR_BGR2GRAY)

            face=self.face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

            for x,y,w,h in face:
                    self.img=cv2.rectangle(self.frame_in_cv2,(x,y),(x+w,y+h),(0,0,255),1)  #making a recentangle to show up and detect the face and setting it position and colour
            
                #making a try and except condition in case of any errors
                #this is the part where we display the output to the user
            cv2.imshow('video', self.frame_in_cv2)
            key=cv2.waitKey(1) 
            
            return self.send_emo()
                    

    def send_emo(self):
                try:
                    analyze = DeepFace.analyze(self.frame_in_cv2,actions=['emotion'])  #same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
                    self.emo = analyze['dominant_emotion']
                    print(self.emo)  #here we will only go print out the dominant emotion also explained in the previous example
                    return self.emo
                except Exception as e:
                    print("no face", e)
                    return e
                 


    
if __name__=="__main__":
    try:
        FaceDetection()
    except Exception as e:
        print(e)