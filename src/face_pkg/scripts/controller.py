import dyna
import rospy
import time
import dyna.motors as mot
import motor_driver as md
from face_pkg.msg import Trans,Motor



class MotorsController():
    def __init__(self):
        rospy.Subscriber("\transformations\hand", Motor, self.hand_controller)
        rospy.Subscriber("\transformations\head", Motor, self.head_controller)
        rospy.Subscriber("\transformations\move", Trans, self.trans_controller)
        if rospy.is_shutdown():
            mot.stop()

    def hand_controller(self,data):
        self.hand_motor = data.motor
        self.hand_pos = data.pos
        mot.hand(self.hand_pos,self.hand_motor)

    def head_controller(self,data):
        self.head_motor = data.motor
        self.head_pos = data.pos
        mot.head(self.head_pos,self.head_motor)

    def trans_controller(self,data):
        self.speed = data.speed
        self.theta = data.theta
        if self.speed <= 0:
            mot.stop()
        else:    
            md.set_cmd_vel(self.speed,self.theta)



