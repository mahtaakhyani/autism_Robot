#!/usr/bin/env python


from logging import shutdown
import rospy
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from nav_msgs.msg import Odometry
# from tf.transformations import quaternion_from_euler
# import tf
import time
import math
from std_msgs.msg import Empty
from motor_driver import RobotMover

class m2wrSimulation():    
    def __init__(self):
	
        # initiliaze        
        rospy.init_node('listener_node', anonymous=False)
        rospy.loginfo("Starting m2wr control")
                
        self.motor_driver = RobotMover()

        # tell user how to stop Bebop
        rospy.loginfo("To stop CTRL + C")
        
        # What function to call when you ctrl + c    
        # rospy.on_shutdown(self.shutdown)
        
        self.odom = Odometry()  
        self.position_x  = 0
        self.position_y  = 0
        self.position_z  = 0
        self.orientation = 0

        self.real_linear_speed_x = 0
        self.real_angular_speed_z = 0

        self.current_time = 0
        self.last_time = 0
    
        
        self.frequencyUpdate = 10
        self.r = rospy.Rate(self.frequencyUpdate)
        t0 = time.time()

        rospy.loginfo('Ready to move')
        

        self.cmd_vel_subscriber  = rospy.Subscriber('/cmd_vel', Twist, self.readCmd_vel)
        self.head_cmd_vel_subscriber  = rospy.Subscriber('/head_cmd_vel', Twist, self.head_Cmd_vel)

        
        ######################################################
        
            

    def readCmd_vel(self,cmd_data):
        print('\n Welcome to velocity function!')

        self.cmd_vel = cmd_data
        print(self.cmd_vel)
        self.linear_speed = self.cmd_vel.linear.x
        self.angular_speed = self.cmd_vel.angular.z

        #Setting the speed to test run speed
        self.tested_angular_speed = 90/1.567
        self.tested_linear_speed = 1000/6.17575

        if self.angular_speed != 0:
            if self.angular_speed > 0:
                self.real_angular_speed_z = abs(self.tested_angular_speed*math.pi/180)*100 #radians
            else:
                self.real_angular_speed_z = -abs(self.tested_angular_speed*math.pi/180)*100
        else:
            self.real_angular_speed_z = 0

        if self.linear_speed != 0 :
            if self.linear_speed > 0:
                self.real_linear_speed_x = abs(self.tested_linear_speed)
            else:
                self.real_linear_speed_x = -abs(self.tested_linear_speed)
           
        else:
            self.real_linear_speed_x = 0

        rospy.loginfo('Cmd_vel command recieved')

        self.motor_driver.set_cmd_vel(self.linear_speed,self.angular_speed)

        self.r.sleep()

    def head_Cmd_vel(self, msg):
        rotation = msg.angular.z

        rospy.loginfo('Head Cmd_vel command recieved')
        self.motor_driver.set_head_cmd_vel(rotation)
        print(rotation)



    


if __name__ == '__main__':
    try:
        m2wrSimulation()
        rospy.spin()
    except rospy.ROSInterruptException:
        print('error')
        pass
