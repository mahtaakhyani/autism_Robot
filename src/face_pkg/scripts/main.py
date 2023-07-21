#!/usr/bin/env python3
import rospy
import rospkg
from std_msgs.msg import String
from face_pkg.msg import Exp
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import base64

import sys


# DO NOT MODIFY
# This is a workaround for the error 'AttributeError: module not found' while importing face_imitation.py through ROS.
# This solution is  based on what is described here: https://www.programcreek.com/python/example/93572/rospkg.RosPack
pkg_dir = rospkg.RosPack().get_path('face_pkg')
sys.path.insert(0, pkg_dir)
import scripts.face_imitation as face_imitation


class FaceImpression():
    def __init__(self): 
        self.cv_bridge = CvBridge()
        rospy.init_node('face_pub', anonymous=False)
        self.publisher = rospy.Publisher(
                '/viz_flow/rgb', String, queue_size=10)
        self.time = rospy.Time.now()
        self.pub = rospy.Publisher('/py_exp_publisher', Exp, queue_size=10)
        self.mood = Exp()
        rospy.Subscriber('/web_exp_publisher', Exp , self.callback)
        # rospy.Subscriber('/camera/image_raw', Image , self.get_frame, queue_size=10)
        rate = rospy.Rate(20) # 20hz
        while not rospy.is_shutdown():
            self.mood.action = 'Facial Expression'
            rate.sleep()


    # def get_frame(self, data):
    #     self.frame = data
        # self.frame_in_cv2 = self.cv_bridge.imgmsg_to_cv2(
        #         self.frame, desired_encoding='passthrough')
        # image_as_str = base64.b64encode(self.frame_in_cv2).decode('utf-8')
        # self.publisher.publish(image_as_str)
        

    def callback(self,data):
        dt = rospy.Time.now() - self.time
        self.mood.time = dt
        self.mood.emotion = data.emotion
        self.mood.auto_imit = data.auto_imit
        rospy.loginfo(self.mood)
        if data.auto_imit:
            
            self.initiate_camera()
            self.pub.publish(self.mood)
        else:
            pass
    

    def initiate_camera(self):
        rospy.loginfo('Auto face emotion detection initiated.')
        self.mood.emotion = str(face_imitation.FaceDetection().main())
        self.pub.publish(self.mood)


if __name__ == '__main__':
    try:
        FaceImpression()
    except rospy.ROSInterruptException:
        pass