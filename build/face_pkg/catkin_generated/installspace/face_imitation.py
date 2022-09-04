# !/usr/bin/env python3
import cv2
from deepface import DeepFace


class FaceDetection():  
    def __init__(self):
        # rospy.init_node('webcam', anonymous=False)
        # self.img_pub = rospy.Publisher('/webcam/image', Image, queue_size=10 )
        self.face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  #getting a haarcascade xml file
        self.face_cascade = cv2.CascadeClassifier()  #processing it for our project
        if not self.face_cascade.load(cv2.samples.findFile(self.face_cascade_name)):  #adding a fallback event
            print("Error loading xml file")



    
    def main(self):
        self.video=cv2.VideoCapture(0)  #requisting the input from the webcam or camera
        while self.video.isOpened():  #checking if are getting video feed and using it
            _,self.frame = self.video.read()
            gray=cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)  #changing the video to grayscale to make the face analisis work properly
            face=self.face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

            for x,y,w,h in face:
                self.img=cv2.rectangle(self.frame,(x,y),(x+w,y+h),(0,0,255),1)  #making a recentangle to show up and detect the face and setting it position and colour
        
            #making a try and except condition in case of any errors
            #this is the part where we display the output to the user
            cv2.imshow('video', self.frame)
            key=cv2.waitKey(1) 
            emo = self.send_emo()
            return emo
                    

    def send_emo(self):
                try:
                    analyze = DeepFace.analyze(self.frame,actions=['emotion'])  #same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
                    self.emo = analyze['dominant_emotion']
                    print(self.emo)  #here we will only go print out the dominant emotion also explained in the previous example
                    return self.emo
                except Exception as e:
                    print("no face", e)
                    return e
                    pass
global f
f = FaceDetection()
f = f.main()

if __name__=="__main__":
    try:
        FaceDetection()
    except Exception as e:
        print(e)