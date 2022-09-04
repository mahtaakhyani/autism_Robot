#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from face_pkg.msg import Exp
import face_pkg.scripts.face_imitation as face_imitation
import sys

class FaceImpression():
    def __init__(self):
        if not hasattr(sys, 'argv'):
            sys.argv  = ['']
        rospy.init_node('face_pub', anonymous=False)
        self.pub = rospy.Publisher('exp', Exp, queue_size=10)
        self.mood = Exp()
        rospy.Subscriber('/web_exp_publisher', Exp , self.callback)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            self.mood.action = 'Facial Expression'
            rate.sleep()


    def callback(self,data):
        # dt = rospy.Time.now() - self.time
        # self.mood.time = dt
        rospy.loginfo(data)
        self.mood.emotion = data.emotion
        self.mood.auto_imit = data.auto_imit
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