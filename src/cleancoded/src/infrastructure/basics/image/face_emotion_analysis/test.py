import rospy
import numpy as np
import cv2
from face_pkg.msg import List
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

import time

def func(data_list):
    cv_bridge=CvBridge()
    arr = []
    l = data_list.list
    for i in range(len(l)):
        arr.append(list(l[i].data))
    # sub.unregister()
    arrrrr= np.array(arr, dtype=np.uint8).reshape((640,480,3))
    # cv2.imshow('Victory',arrrrr)
    frame_in_ros = cv_bridge.cv2_to_imgmsg(arrrrr)
    frame_in_ros.encoding = "rgb8"
    msg = Image()
    msg = frame_in_ros
    pub.publish(msg)
    cv2.imwrite('testaki.jpg',arrrrr)


rospy.init_node('test',anonymous=False)
pub = rospy.Publisher('/testaki',Image,queue_size=10)
sub = rospy.Subscriber('/image_cv2',List,func)
rospy.spin()