#!/usr/bin/env python3
from time import time
import rospy
from std_msgs.msg import String
from face_pkg.msg import Exp
import face_imitation

class FaceImpression():
    def __init__(self) -> None:
            rospy.Subscriber('exp', Exp , self.callback)
            rospy.init_node('face_pub', anonymous=False)
            self.pub = rospy.Publisher('exp', Exp, queue_size=10)
            self.mood = Exp()
    def face_publisher(self):
        time = rospy.Time.now()
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            hello_str =  " %s" % rospy.get_time()
            dt = rospy.Time.now() - time
            self.mood.time = dt
            self.mood.action = 'Facial impression'
            rate.sleep()

    def callback(self,data):
        rospy.loginfo(data)
        self.mood.emotion = data.emotion
        self.mood.auto_imit = data.auto_imit
        if data.auto_imit:
            rospy.loginfo('Auto face emotion detection initiated. Camera activating...')
            self.mood.emotion = face_imitation.FaceDetection().main(data.auto_imit)
        self.pub.publish(self.mood)


if __name__ == '__main__':
    try:
        FaceImpression().face_publisher()
    except rospy.ROSInterruptException:
        pass