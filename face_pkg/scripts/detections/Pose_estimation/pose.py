# Import Libraries
import cv2
import time
import mediapipe as mp
import numpy as np

from .matrix import gridding as gd



class MeshDetector():
	def __init__(self, image, mp_holistic, results):

		# gathering all landmarks for global use
		self.face_landmarks = (results.face_landmarks , mp_holistic.FACEMESH_TESSELATION )
		self.right_hand_landmarks = (results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
		self.left_hand_landmarks = (results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
		self.pose_landmarks = (results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

		# Adding simple gridding system to each frame for furthur analysis
		self.image = self.pointing(image)

		# Draw landmarks and connections between them
		self.draw(self.image, self.face_landmarks, thickness=1, color=(125,125,125))
		self.draw(self.image, self.right_hand_landmarks, radius=5)
		self.draw(self.image, self.left_hand_landmarks, radius=5)
		self.draw(self.image, self.pose_landmarks, thickness=1, radius=2, color=(0,255,255))
		# Returning the processed image back to the main module
		# self.feedback(image)
		# cv2.imshow('f',image)
	def pointing(self, image):

		return image
		


	def draw(self,image, landmark, thickness=2 ,radius=0, color=(255,0,255)):
				# Initializing the drawing utils for drawing the facial landmarks on image
			mp_drawing = mp.solutions.drawing_utils
			# Drawing the Facial Landmarks
			mp_drawing.draw_landmarks(
			image,
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
			return image

	
	def feedback(self):
		return self.image

if __name__ == "__main__":
	MeshDetector()