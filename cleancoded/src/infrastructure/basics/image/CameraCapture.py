#!/usr/bin/env python3
from typing import Any
import cv2
import numpy as np
import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import CameraInfo, Image
from std_msgs.msg import Float64MultiArray, String
from face_pkg.msg import Array3D,List
from waiting import wait


class CameraCapture:
    height = 800
    width = 600
    rate = 20
    queue_size = 10
    modif_image = np.zeros((640,480,3))
    rospy.init_node("opencv_client", anonymous=False)
    pub = rospy.Publisher('/image_cv2',List,queue_size=10)


    def __init__(self) -> None:
        
        rospy.Subscriber("/camera_info", CameraInfo, self.syncinfo)
        rospy.Subscriber(
            "/image_raw", Image, self.convert_frame, callback_args=False, queue_size=1, buff_size=2**36
        )


    def syncinfo(self, info):  # sync camera video stream info
        self.height = info.height
        self.width = info.width
    
    def convert_frame(self, data, cv2window=False):
        cv_bridge = CvBridge()
        # try:
        frame_in_cv2 = cv_bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
        new_a_shape = (-1,) + frame_in_cv2.shape[2:] # to get rid of the first dimension
        b = np.split(frame_in_cv2.reshape(new_a_shape), frame_in_cv2.shape[0])
        frame = np.array(b)

        self.modif_image = cv2.resize(frame, (self.height, self.width))
        self.modif_image = cv2.cvtColor(self.modif_image, cv2.COLOR_BGR2RGB)
        # Convert the NumPy array to the float type
        # To improve performance, optionally mark the image as not writeable to pass by reference.
        self.modif_image.flags.writeable =False
        te = Array3D()
        tem = List()
        temp = list()
        msg = List()
        pub = rospy.Publisher('/testaki',Image,queue_size=10)
        llll=self.modif_image.tolist()
        for i in llll:
            for j in i:
                    obj=Array3D()
                    obj.data=j
                    tem.list.append(obj)
        
        cv_bridge=CvBridge()
        arr = []
        l = tem.list
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
        if cv2window:  # whether to show the frames in an opencv window apart from ROS image_view or not
            cv2.imshow("output window", self.modif_image)
        
        self.pub.publish(tem)


if __name__ == "__main__":
        camcap = CameraCapture()
        rospy.spin()
