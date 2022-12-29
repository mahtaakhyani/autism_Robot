#!/usr/bin/env python3
import dyna
import rospy
import time
from dyna import motors as mot
import motor_driver as md
from face_pkg.msg import Motor



class MotorsController():
    def __init__(self):
        # rospy.Subscriber("\transformations\hand", Motor, self.hand_controller)
        # rospy.Subscriber("\transformations\head", Motor, self.head_controller)
        # rospy.Subscriber("\transformations\move", Trans, self.trans_controller)

        rospy.Subscriber("/head_cmd_vel", Motor, self.head_controller)
        if rospy.is_shutdown():
            mot.stop()

    def hand_controller(self,data):
        self.hand_motor = data.motor
        self.hand_pos = data.pose
        mot.hand(self.hand_pos,self.hand_motor)

    def head_controller(self,data):
        self.head_motor = data.motor
        self.head_pos = data.pose
        mot().head(self.head_pos,self.head_motor)

    def trans_controller(self,data):
        self.speed = data.speed
        self.theta = data.theta
        if self.speed <= 0:
            mot.stop()
        else:    
            md.set_cmd_vel(self.speed,self.theta)



if __name__ == '__main__':
    rospy.init_node('motors_controller', anonymous=True)
    try:
        mc = MotorsController()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    