# Import Libraries
from typing import Any
import cv2
import rospy
import mediapipe as mp
import numpy as np
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge
from face_pkg.msg import List


# from .matrix import gridding as gd



class MeshDetector():
	rate = 20
	mp_holistic = mp.solutions.holistic
	image = np.zeros((640,480,3))
	imgmsg = Image()

	def __init__(self):
		rospy.Subscriber("/camera_info", CameraInfo, self.syncinfo, queue_size=10)
		rospy.Subscriber('/image_cv2',List,self.catch)


	def syncinfo(self, info):  # sync camera video stream info
		self.height = info.height
		self.width = info.width		

	def catch(self,_):
		arr = []
		l = _.list
		for i in range(len(l)):
			arr.append(list(l[i].data))
        # sub.unregister()
		self.arrrrr= np.array(arr, dtype=np.uint8).reshape((640,480,3))
		self.analyze(self.arrrrr)
		
	def convert_back(self,_):
		cv_bridge=CvBridge()
		frame_in_ros = cv_bridge.cv2_to_imgmsg(_)
		frame_in_ros.encoding = "rgb8"
		msg = Image()
		msg = frame_in_ros
		cv2.imwrite('testaki.jpg',_)
		return msg


	def analyze(self,frame): #landmarks dtection -> face+pose+hands
		self.image = cv2.resize(frame, (self.height, self.width))
		# # Convert the image to 8-bit unsigned integer data type
		# image_8u = cv2.convertScaleAbs(self.image)

		# Convert the image to a NumPy array with three color channels
		image_array = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
		with self.mp_holistic.Holistic(
			# max_num_faces=1,  # number of faces to track in each frame
			refine_face_landmarks=True,  # includes iris landmarks in the face mesh model
			min_detection_confidence=0.5,
			min_tracking_confidence=0.5) as face_mesh:
			results = face_mesh.process(image_array)
		
		# gathering all landmarks for global use
		self.face_landmarks = (results.face_landmarks , self.mp_holistic.FACEMESH_TESSELATION )
		self.right_hand_landmarks = (results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
		self.left_hand_landmarks = (results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
		self.pose_landmarks = (results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS)

		# Draw landmarks and connections between them
		self.draw(self.face_landmarks, thickness=1, color=(125,125,125))
		self.draw(self.right_hand_landmarks, radius=5)
		self.draw(self.left_hand_landmarks, radius=5)
		self.draw(self.pose_landmarks, thickness=1, radius=2, color=(0,255,255))
		# Adding simple gridding system to each frame for furthur analysis
		# self.image = self.pointing(image)

		pub = rospy.Publisher("/image_raw/landmarked", Image, queue_size=10)
		msg = self.convert_back(self.image)
		pub.publish(msg)
		# Returning the processed image back to the main module
		return [self.face_landmarks,self.left_hand_landmarks,self.right_hand_landmarks,self.pose_landmarks]

	def pointing(self, image):

		return image
		


	def draw(self, landmark, thickness=2 ,radius=0, color=(255,0,255)):

				# Initializing the drawing utils for drawing the facial landmarks on image
			mp_drawing = mp.solutions.drawing_utils
			# Drawing the Facial Landmarks
			mp_drawing.draw_landmarks(
			self.image,
			landmark[0],
			landmark[1],
			mp_drawing.DrawingSpec(
				color=color[::-1],
				thickness=0,
				circle_radius=radius
			),
			mp_drawing.DrawingSpec(
				color=color,
				thickness=thickness,
				circle_radius=radius
			)
			)
			return self.image

	


if __name__ == "__main__":
		rospy.init_node("landmark_detection", anonymous=False)
		md = MeshDetector()
		rospy.spin()

