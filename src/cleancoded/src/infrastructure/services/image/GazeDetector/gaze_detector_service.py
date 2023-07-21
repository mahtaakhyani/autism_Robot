import rospy
from sensor_msgs.msg import Image
from face_pkg.srv import gaze
from gaze_estimator import GazePosition


img_msg = Image()

def callback(_):
    try:
        g_pose = GazePosition(img_msg).__str__()
        return g_pose
    except BaseException as bex:
        return bex
    pass

def frame_pass(_):
    img_msg = _
    pass

rospy.init_node('gaze_detector',anonymous=False)
rospy.Service('gaze_pose',gaze,callback)
rospy.Subscriber('/image_raw',Image,frame_pass)
rospy.spin()