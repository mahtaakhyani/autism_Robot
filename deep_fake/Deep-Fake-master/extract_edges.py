# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# image = cv2.imread("C:\\Users\\mahta\\OneDrive\\Documents\\GitHub\\autism_Robot\\src\\deep_fake\\logo.png")
# image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# g = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
# edge = cv2.Canny(g, 60, 180)
# contours,h = cv2.findContours(edge, 
#                                cv2.RETR_EXTERNAL,
#                                cv2.CHAIN_APPROX_NONE)
                               
# # contours, hierarchy = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# # for c in contours:
# #     hull = cv2.convexHull(c)
# #     image = np.zeros_like(image)
# #     cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)
# print(contours)
# image = np.zeros_like(image)
# cv2.drawContours(image, contours[0], -1, (0,0,255), thickness = 2)
# while True:
#     cv2.imshow("counters",image)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()

# Python code to find the co-ordinates of 
# the contours detected in an image. 
import numpy as np 
import cv2 

image = "C:\\Users\\mahta\\OneDrive\\Documents\\GitHub\\autism_Robot\\src\\deep_fake\\logo.png"
# Reading image 
font = cv2.FONT_HERSHEY_COMPLEX 
img2 = cv2.imread(image, cv2.IMREAD_COLOR) 

# Reading same image in another 
# variable and converting to gray scale. 
img = cv2.imread(image, cv2.IMREAD_GRAYSCALE) 

# Converting image to a binary image 
# ( black and white only image). 
_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY) 
# Detecting contours in image. 
contours, _= cv2.findContours(threshold, cv2.RETR_EXTERNAL, 
                            cv2.CHAIN_APPROX_SIMPLE) 
contours = sorted(contours, key=cv2.contourArea, reverse=True)
# Going through every contours found in the image. 
coordinates = []
img2 = np.zeros_like(img2)
for cnt in contours : 

    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 

    # draws boundary of contours. 
    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 2) 

    # Used to flatted the array containing 
    # the co-ordinates of the vertices. 
    n = approx.ravel() 
    i = 0

    for j in n : 
        if(i % 2 == 0): 
            x = n[i] 
            y = n[i + 1] 
            coordinates.append((x,y))

            # String containing the co-ordinates. 
            string = str(x) + " " + str(y) 

            if(i == 0): 
                # text on topmost co-ordinate. 
                cv2.putText(img2, "Arrow tip", (x, y), 
                                font, 0.5, (255, 0, 0)) 
            else: 
                # text on remaining co-ordinates. 
                cv2.putText(img2, string, (x, y), 
                        font, 0.5, (0, 255, 0)) 
        i = i + 1

# Showing the final image. 
cv2.imshow('image2', img2) 
print(coordinates)
# Exiting the window if 'q' is pressed on the keyboard. 
if cv2.waitKey(0) & 0xFF == ord('q'): 
    cv2.destroyAllWindows()


class obj():
    def extract_edges(self,image):
        img2 = cv2.imread(image, cv2.IMREAD_COLOR) 
        # Reading same image in another 
        # variable and converting to gray scale. 
        img = cv2.imread(image, cv2.IMREAD_GRAYSCALE) 
        # Converting image to a binary image 
        # ( black and white only image). 
        _, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY) 
        # Detecting contours in image. 
        contours, _= cv2.findContours(threshold, cv2.RETR_EXTERNAL, 
                                    cv2.CHAIN_APPROX_SIMPLE) 
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        # Going through every contours found in the image. 
        coordinates = []
        img2 = np.zeros_like(img2)
        for cnt in contours : 

            approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 

            # draws boundary of contours. 
            cv2.drawContours(img2, [approx], 0, (0, 0, 255), 2) 

            # Used to flatted the array containing 
            # the co-ordinates of the vertices. 
            n = approx.ravel() 
            i = 0

            for j in n : 
                if(i % 2 == 0): 
                    x = n[i] 
                    y = n[i + 1] 
                    coordinates.append((x,y))

        return coordinates



