#!/usr/bin/env python
import rospy
import serial
import time
from multi_parrot_blue.srv import *
from std_msgs.msg import String


def parrot_client(command):
    rospy.wait_for_service('blue_serial_handler/blueparrot')
    try:
        parrot_connection = rospy.ServiceProxy('blue_serial_handler/blueparrot', BlueParrot)
        result = parrot_connection(command)
        return result.result
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def dance(number = 1):
    res = parrot_client('G1 S%d'%number)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def blink(pwm = 120):
    res = parrot_client('G2 S%d'%pwm)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def mouth(pwm = 0): # open and close the mouth 255 -> open mouth      0 -> close mouth
    res = parrot_client('G3 S%d'%pwm)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def open_eye(pwm = 130):
    res = parrot_client('G4 S%d'%pwm)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def close_eye(pwm = 80):
    res = parrot_client('G5 S%d'%pwm)
    if(res.find("DONE") != 1):
        print ("done")
    else:
        print("not done")

def talk():
    mouth(240)
    time.sleep(.5)
    mouth(0)
    time.sleep(.5)
    mouth(240)
    time.sleep(.5)
    mouth(0)



def parrot_commands(data):
    if(str(data.data) == '100' ):   # dance
        dance()
    elif(str(data.data) == '101' ):  # blink
        blink()
    elif(str(data.data) == '102' ): # open mouth
        mouth(240)
    elif(str(data.data) == '103' ): # close mouth
        mouth(0)
    elif(str(data.data) == '104' ): # open eye
        open_eye()
    elif(str(data.data) == '105' ): # close eye
        close_eye()
    elif(str(data.data) == '106'): # talk
        talk()

def audio_command(data):
    text = data.data
    if text.find("shutup") == -1:
        talk()


def ros_init():
    rospy.init_node('blue_parrot', log_level=rospy.DEBUG)
    rospy.Subscriber('/parrot/1/parrot_commands', String, parrot_commands, queue_size=10)
    rospy.Subscriber("/parrot/1/audio_player", String, audio_command, queue_size=10)
    rospy.spin()


if __name__ == "__main__":
    ros_init()
