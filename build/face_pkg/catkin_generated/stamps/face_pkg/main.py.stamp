#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from face_pkg.msg import Exp
import face_imitation

class FaceImpression():
    def __init__(self):
            rospy.Subscriber('web_exp_publisher', Exp , self.callback)
            rospy.init_node('face_pub', anonymous=False)
            self.pub = rospy.Publisher('exp', Exp, queue_size=10)
            self.mood = Exp()

    def face_publisher(self):
        self.time = rospy.Time.now()
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            self.mood.action = 'Facial Expression'
            rate.sleep()

    def callback(self,data):
        dt = rospy.Time.now() - self.time
        self.mood.time = dt
        rospy.loginfo(data)
        self.mood.emotion = data.emotion
        self.mood.auto_imit = data.auto_imit
        if data.auto_imit:
            self.initiate_camera()
        else:
            self.pub.publish(self.mood)
    

    def initiate_camera(self):
        rospy.loginfo('Auto face emotion reaction initiated.')
        self.mood.emotion = 'output=',f.main()
        self.pub.publish(self.mood)


if __name__ == '__main__':
    try:
        f = face_imitation.FaceDetection()
        FaceImpression().face_publisher()
    except rospy.ROSInterruptException:
        pass