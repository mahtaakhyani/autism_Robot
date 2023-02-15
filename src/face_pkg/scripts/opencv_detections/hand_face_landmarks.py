# Import Libraries
import cv2
import time
import mediapipe as mp
import numpy as np
import holisticcustom as hc


class MeshDetector():
	def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
		# Initializing the drawing utils for drawing the facial landmarks on image
		mp_drawing = mp.solutions.drawing_utils

		# Grabbing the Holistic Model from Mediapipe and Initializing the Model
		mp_holistic = hc
		holistic_model = mp_holistic.Holistic(
			min_detection_confidence=0.5,
			min_tracking_confidence=0.5,
			refine_face_landmarks=True
		)

		# (0) in VideoCapture is used to connect to your computer's default camera
		capture = cv2.VideoCapture(0)

		# Initializing current time and precious time for calculating the FPS
		previousTime = 0
		currentTime = 0

		while capture.isOpened():
			# capture frame by frame
			ret, frame = capture.read()

			# resizing the frame for better view
			frame = cv2.resize(frame, (800, 600))

			# Converting the from BGR to RGB
			image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			# Making predictions using holistic model
			# To improve performance, optionally mark the image as not writeable to
			# pass by reference.
			image.flags.writeable = False
			results = holistic_model.process(image)
			image.flags.writeable = True

			# Converting back the RGB image to BGR
			image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

			# Drawing the Facial Landmarks
			mp_drawing.draw_landmarks(
			image,
			results.face_landmarks,
			mp_holistic.FACEMESH_IRISES,
			mp_drawing.DrawingSpec(
				color=(255,0,255),
				thickness=0,
				circle_radius=0
			),
			mp_drawing.DrawingSpec(
				color=(0,255,255),
				thickness=2,
				circle_radius=0
			)
			)
			# PoseLandmark
			# mp_drawing.draw_landmarks(
			# image,
			# results.pose_landmarks,
			# mp_holistic.PoseLandmark,
			# mp_drawing.DrawingSpec(
			# 	color=(255,0,255),
			# 	thickness=0,
			# 	circle_radius=0
			# ),
			# mp_drawing.DrawingSpec(
			# 	color=(0,255,255),
			# 	thickness=2,
			# 	circle_radius=0
			# )
			# )
			FACEMESH_RIGHT_IRIS = list(set([i[0] for i in (mp_holistic.FACEMESH_CONTOURS.intersection(mp_holistic.FACEMESH_RIGHT_EYE))]))
			FACEMESH_RIGHT_IRIS.sort()
			iris_xyz = [str(i)+': \n'+str(results.face_landmarks.landmark[i]) for i in FACEMESH_RIGHT_IRIS]
			# extract iris position from landmarks
			# for i in iris_xyz:
			# 	print(i)
			
			iris_landmarks = [results.face_landmarks.landmark[i] for i in FACEMESH_RIGHT_IRIS]
			# extract pupil position from landmarks
			self.pupil_tracker(image, iris_landmarks)


			# Drawing Right hand Land Marks
			mp_drawing.draw_landmarks(
			image,
			results.right_hand_landmarks,
			mp_holistic.HAND_CONNECTIONS
			)

			# Drawing Left hand Land Marks
			mp_drawing.draw_landmarks(
			image,
			results.left_hand_landmarks,
			mp_holistic.HAND_CONNECTIONS
			)
			
			# Calculating the FPS
			currentTime = time.time()
			fps = 1 / (currentTime-previousTime)
			previousTime = currentTime
			
			# Displaying FPS on the image
			# cv2.putText(image, str(int(fps))+" FPS", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
			cv2.putText(image, str(float(results.face_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE].x))+" right eye", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

			# Display the resulting image
			cv2.imshow("Facial and Hand Landmarks", image)
			# Code to access landmarks
			# for landmark in mp_holistic.HandLandmark:
			# 	print(landmark, landmark.value)

			# Enter key 'q' to break the loop
			if cv2.waitKey(5) & 0xFF == ord('q'):
				break

		# When all the process is done
		# Release the capture and destroy all windows
		capture.release()
		cv2.destroyAllWindows()



	def pupil_tracker(self, image, landmarks):
			# extract iris position from landmarks
			iris = [[i.x,i.y,i.z] for i in landmarks]
			iris = np.array(iris)
			# get iris center
			iris_center = np.mean(iris,axis=0)
			print(iris_center)
			# get iris radius
			# iris_radius = int(np.linalg.norm(iris[0][0] - iris[3][0]) / 2)
			# # draw iris
			# cv2.circle(image, tuple(iris_center), iris_radius, (0, 255, 0), 2)
			# # get pupil center
			# pupil_center = np.mean(iris[1:3], axis=0).astype(np.int)
			# # get pupil radius
			pupil_radius = int(np.linalg.norm(iris[0][-1] - iris[0][0]) / 2)
			# draw pupil
			cv2.circle(image, tuple(iris_center), pupil_radius, (255, 0, 0))
			return image


if __name__ == "__main__":
	MeshDetector()