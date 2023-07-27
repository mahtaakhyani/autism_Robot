import rospy
from face_pkg.srv import gaze
from sensor_msgs.msg import Image
import numpy as np
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import infrastructure.basics.image.landmarks_detection.pose as pose

points = np.array([
            (0.0, 0.0, 0.0),  # Nose tip
            (0, -63.6, -12.5),  # Chin
            (-43.3, 32.7, -26),  # Left eye, left corner
            (43.3, 32.7, -26),  # Right eye, right corner
            (-28.9, -28.9, -24.1),  # Left Mouth corner
            (28.9, -28.9, -24.1)  # Right mouth corner
        ])


pm=pose.MeshDetector()

srv = rospy.ServiceProxy('gaze_pose',gaze)
def callservice(frame):
    results = pm.analyze(frame)
    srv.call(frame,results[0])


rospy.init_node("testservice")
rospy.Subscriber("/image_raw",Image,callservice)

print(srv)
# rospy.spin()