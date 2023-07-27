import cv2
from statistics import mode
import random
from deepface import DeepFace



class FaceDetection():  
    def __init__(self):
        self.frame_msgs = None
        self.face_cascade_name = None
        self.face_cascade = None
        self.img = None
        self.face_width = None
        self.global_dominant_emotion = []
        
    def prequisites(self,image):
        self.frame_msgs = image
        self.face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  #getting a haarcascade xml file
        self.face_cascade = cv2.CascadeClassifier()  #processing it for our project
        if not self.face_cascade.load(cv2.samples.findFile(self.face_cascade_name)):  #adding a fallback event
            print("Error loading xml file")
        gray = cv2.cvtColor(self.frame_msgs, cv2.COLOR_BGR2GRAY)
        face=self.face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

        for x,y,w,h in face:
                self.img=cv2.rectangle(self.frame_msgs,(x,y),(x+w,y+h),
                (random.randint(0,255),random.randint(0,255),random.randint(0,255)),1)  #making a recentangle to show up and detect the face and setting it position and colour
                self.face_width = h
        

    def emotion_detection(self,image):
            self.prequisites(image)
            analyze = DeepFace.analyze(self.frame_msgs,actions=['emotion'], enforce_detection=False)  #same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
            result = analyze[:]
            
            return result



    def __str__(self,image):
        feedback = self.emotion_detection(image)
        emotion = feedback[0]['emotion']
        dominant = feedback[0]['dominant_emotion']
        if len(self.global_dominant_emotion) <= 50:
            self.global_dominant_emotion.append(str(dominant))
        else:
            self.global_dominant_emotion = []
            self.global_dominant_emotion.append(str(dominant))

        overall_emotion = mode(self.global_dominant_emotion)
        # Sorting emotions by higher propablity values gotten
        sorted_values = sorted(emotion.items(), key=lambda item: item[1])[::-1]
        prettied_dict = [str(i)+' : '+str(round(j,6)) for i,j in sorted_values]+['Dominant Emotion : '+str(overall_emotion)]
        # Converting to string to display on the camera frame output
        prettied_str = '\n'.join(prettied_dict)

        return prettied_str