#!/usr/bin/env python3
import rospy
import rospkg
from std_msgs.msg import String
from face_pkg.msg import Exp
import sys

# DO NOT MODIFY
# This is a workaround for the error 'AttributeError: module not found' while importing face_imitation.py through ROS.
# This solution is  based on what is described here: https://www.programcreek.com/python/example/93572/rospkg.RosPack
pkg_dir = rospkg.RosPack().get_path('face_pkg')
sys.path.insert(0, pkg_dir)
import scripts.face_imitation as face_imitation


class FaceImpression():
    def __init__(self):
        rospy.init_node('face_pub', anonymous=False)
        self.time = rospy.Time.now()
        self.pub = rospy.Publisher('exp', Exp, queue_size=10)
        self.mood = Exp()
        rospy.Subscriber('/web_exp_publisher', Exp , self.callback)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            self.mood.action = 'Facial Expression'
            rate.sleep()


    def callback(self,data):
        dt = rospy.Time.now() - self.time
        self.mood.time = dt
        self.mood.emotion = data.emotion
        self.mood.auto_imit = data.auto_imit
        rospy.loginfo(self.mood)
        if data.auto_imit:
            self.initiate_camera()
        else:
            self.pub.publish(self.mood)
    

    def initiate_camera(self):
        rospy.loginfo('Auto face emotion reaction initiated.')
        self.mood.emotion = str(face_imitation.FaceDetection().main())
        self.pub.publish(self.mood)


if __name__ == '__main__':
    try:
        FaceImpression()
    except rospy.ROSInterruptException:
        pass