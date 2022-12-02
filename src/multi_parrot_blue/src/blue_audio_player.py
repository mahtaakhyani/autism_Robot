#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import pygame
import time
import math



def play_sound(data):
    text = data.data
    if text.find("shutup") == -1:
        pygame.mixer.stop()
        pygame.mixer.Sound.play(pygame.mixer.Sound(data.data))
    elif text.find("shutup") != -1:
        stop_sound()


def stop_sound():
    pygame.mixer.stop()



def ros_init():
    rospy.init_node('blue_audio_player', log_level=rospy.DEBUG)
    rospy.Subscriber("/parrot/1/audio_player", String, play_sound, queue_size=10)


def pygame_init():
    pygame.mixer.init()
    if pygame.mixer.get_init() is None:
        print("mixer initialization is NOT successful")



if __name__ == "__main__":
    ros_init()
    pygame_init()
    rospy.spin()
