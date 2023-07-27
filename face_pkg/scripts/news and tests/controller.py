#!/usr/bin/env python3
# import rospy
import time
from dynatest import Dynamixel as dyna
# import motor_driver as md
# from face_pkg.msg import Motor



class MotorsController():
    def __init__(self):
        parser = argparse.ArgumentParser(
        description='If you know the port enter it using --port\n Set Dynamixel IDs assigned to different joints using --head, --neck, --lhand, --rhand\n Set --speed')
        parser.add_argument(
                    '--head', type=str,
                    help='e.g., 1,2,3,etc.')
        parser.add_argument(
                    '--neck', type=str,
                    help='e.g., 1,2,3,etc.')
        parser.add_argument(
                    '--lhand', type=str,
                    help='e.g., 1,2,3,etc.')
        parser.add_argument(
                    '--rhand', type=str,
                    help='e.g., 1,2,3,etc.')
        parser.add_argument(
                    '--speed', type=str,
                    help='e.g., 100,etc.')
        parser.add_argument(
                    '--port', type=str,
                    help='e.g., COM8 (Windows), /dev/ttyUSB0 (Linux)')

        args = parser.parse_args()

        dyna()
        # rospy.Subscriber("\transformations\hand", Motor, self.hand_controller)
        # rospy.Subscriber("\transformations\head", Motor, self.head_controller)
        # rospy.Subscriber("\transformations\move", Trans, self.trans_controller)

        # rospy.Subscriber("/cmd_vel", Motor, self.controller_spiliter)
        # if rospy.is_shutdown():
        #     exit()
    
    def controller_spiliter(self,data):
        if data.joint == 'hand': self.hand_controller(data)
        if data.joint == 'head': self.head_controller(data)

    def hand_controller(self,data):
        if data.motor == 0:
            if args.__getattribute__('lhand'): dynamixel_id = args.__getattribute__('lhand')
            else: dynamixel_id = 5
        if data.motor == 1:
            if args.__getattribute__('rhand'): dynamixel_id = args.__getattribute__('rhand')
            else: dynamixel_id = 6
        
        dyna().gotodegree(dynamixel_id, data.pose)

    def head_controller(self,data):
        if data.motor == 0:
                    if args.__getattribute__('head'): dynamixel_id = args.__getattribute__('head')
                    else: dynamixel_id = 7
        if data.motor == 1:
                    if args.__getattribute__('neck'): dynamixel_id = args.__getattribute__('neck')
                    else: dynamixel_id = 4
                
        dyna().gotodegree(dynamixel_id, data.pose)

    # def trans_controller(self,data):
    #     self.speed = data.speed
    #     self.theta = data.theta
    #     if self.speed <= 0:
    #         mot.stop()
    #     else:    
    #         md.set_cmd_vel(self.speed,self.theta)



if __name__ == '__main__':
    # rospy.init_node('motors_controller', anonymous=True)
    try:
        mc = MotorsController()
        # rospy.spin()
    except :
        pass
    