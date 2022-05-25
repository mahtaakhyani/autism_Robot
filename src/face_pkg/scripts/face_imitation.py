#!/usr/bin/env python3
import rospy
from face_pkg.msg import Exp
import cv2
# from cv_bridge import CvBridge
from fer import FER
import parser
from std_msgs.msg import String
# from sensor_msgs.msg import Image


class FaceDetection():  
    def __init__(self):
        # rospy.init_node('webcam', anonymous=False)
        # self.img_pub = rospy.Publisher('/webcam/image', Image, queue_size=10 )
        self.detector = FER()
        face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  #getting a haarcascade xml file
        self.face_cascade = cv2.CascadeClassifier()  #processing it for our project
        if not self.face_cascade.load(cv2.samples.findFile(face_cascade_name)):  #adding a fallback event
            print("Error loading xml file")

        
    def main(self,msg):
        # bridge = CvBridge()
        self.video=cv2.VideoCapture(0)  #requesting the input from the webcam or camera
        self.rate = rospy.Rate(500)  
        _,self.frame = self.video.read()
        self.frame = cv2.flip(self.frame, 0)
        # self.imgMsg = bridge.cv2_to_imgmsg(self.frame, "bgr8")
        # self.img_pub.publish(self.imgMsg)
        while not rospy.is_shutdown():
            try:
                gray=cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)  #changing the video to grayscale to make the face analisis work properly
                face=self.face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
                self.mood = self.detector.top_emotion(self.frame)[0]
                if self.mood == None:
                    self.mood = 'neutral'
                return self.mood


            
            except Exception as e:
                rospy.loginfo(rospy.get_caller_id() + "some error in FER \n%s", e)

            key=cv2.waitKey(1)
            self.rate.sleep()

            if key==ord('q'):   # here we are specifying the key which will stop the loop and stop all the processes going
                self.video.release()
                break
            if not msg:
                return 'Auto Deactivated'

if __name__=="__main__":
    try:
        FaceDetection().main()
    except:
        pass