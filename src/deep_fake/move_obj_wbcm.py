import time
from cv2 import rotate
import cv2
import numpy as np
import os

# ****
RIGHT_BROW = list(range(18, 23))
LEFT_BROW = list(range(23,28))
LEFT_TOP_EYELID = list(range(43,47))
LEFT_BOTTOM_EYELID = list(range(47,49))
RIGHT_TOP_EYELID = list(range(37,41))
RIGHT_BOTTOM_EYELID = list(range(41,43))
NOSE_BRIDGE_POINTS = list(range(27, 31))
LOWER_NOSE_POINTS = list(range(31, 36))
TOP_OUTER_LIP = list(range(49,56))
TOP_INNER_LIP = list(range(61,65))
BOTTOM_OUTER_LIP = list(range(56,61))
BOTTOM_INNER_LIP = list(range(65,70))
JAWLINE_POINTS = list(range(0, 17))
# *****

features_dir = '/features/'
ext = '.jpg'
# RIGHT_BROW = features_dir + 'right_brow' + ext
# LEFT_BROW = features_dir + 'left_brow' + ext
# LEFT_TOP_EYELID = features_dir + 'LEFT_TOP_EYELID' + ext
# LEFT_BOTTOM_EYELID = features_dir + 'LEFT_BOTTOM_EYELID' + ext
# RIGHT_TOP_EYELID = features_dir + 'RIGHT_TOP_EYELID' + ext
# RIGHT_BOTTOM_EYELID = features_dir + 'right_brow' + ext
# NOSE_BRIDGE_POINTS = features_dir + 'right_brow' + ext
# LOWER_NOSE_POINTS = features_dir + 'right_brow' + ext
# TOP_OUTER_LIP = features_dir + 'right_brow' + ext
# TOP_INNER_LIP = features_dir + 'right_brow' + ext
# BOTTOM_OUTER_LIP = features_dir + 'right_brow' + ext
# BOTTOM_INNER_LIP = features_dir + 'right_brow' + ext
# JAWLINE_POINTS = features_dir + 'right_brow' + ext
path = "C:\\Users\\mahta\\Documents\\GitHub\\autism_Robot\\src\\deep_fake\\shape_predictor_68_face_landmarks.dat"
img = "C:\\Users\\mahta\\Documents\\GitHub\\autism_Robot\\src\\deep_fake\\Untitled-1.png"
# Object class to insert logo
class Object:
    def __init__(self, start_x=100, start_y=100, size=50):
        self.logo_org = cv2.imread(img)
        self.size = size
        self.logo = cv2.resize(self.logo_org, (self.size, self.size))
        self.img2gray = cv2.cvtColor(self.logo, cv2.COLOR_BGR2GRAY)
        # Converting image to a binary image 
        # ( black and white only image).  
        _, logo_mask = cv2.threshold(self.img2gray, 1, 255, cv2.THRESH_BINARY)
        self.logo_mask = logo_mask
        # print(self.logo_mask)
        self.on_mask = False
        self.coordinates = self.extract_edges()
        self.x , self.y = self.coordinates


    def extract_edges(self):
        img2 = self.logo_org
        blur = cv2.GaussianBlur(img2, (5, 5),
                       cv2.BORDER_DEFAULT)
        ret, thresh = cv2.threshold(blur, 200, 255,
                           cv2.THRESH_BINARY_INV)
        # Detecting contours in image. 
        contours, _= cv2.findContours(self.logo_mask, cv2.RETR_EXTERNAL, 
                                    cv2.CHAIN_APPROX_SIMPLE) 
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        # Going through every contours found in the image. 
        coordinates = []
        
        blank = np.zeros(thresh.shape[:2],
                        dtype='uint8')
        cv2.drawContours(blank, contours, -1,
                        (255, 0, 0), 1)
                        
        img2 = np.zeros_like(img2)
        for cnt in contours : 

            approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True) 

            # draws boundary of contours. 
            img2 = cv2.drawContours(img2, [approx], 0, (0, 0, 255), 2) 

            # Used to flatted the array containing 
            # the co-ordinates of the vertices. 
            n = approx.ravel() 
            i = 0

            for j in n : 
                if(i % 2 == 0): 
                    x = n[i] 
                    y = n[i + 1] 
                    coordinates.append((x,y))
                    
        # cv2.imshow('img2', img2)
        return (coordinates[0][0], coordinates[0][1])

    def fit(self, shape = [RIGHT_BROW]):
        max_x = shape.max(axis=0)[0]
        max_y = shape.max(axis=0)[1]
        min_x = shape.min(axis=0)[0]
        min_y = shape.min(axis=0)[1]
        return self.angle_between((max_x, max_y), (min_x, min_y))
        
    def angle_between(self, p1, p2):
        xDiff = p2[0] - p1[0]
        yDiff = p2[1] - p1[1]

        return np.degrees(np.arctan2(yDiff, xDiff))
            



    def insert_object(self, frame):
        roi = frame[self.y-int(self.size/2):self.y + int(self.size/2), self.x-int(self.size/2):self.x + int(self.size/2)]
        (h, w) = self.logo.shape[:2]
        self.rotation_radius = 45
        # rotate our image by 45 degrees around the center of the image
        self.x, self.y = self.find_templates(roi, 0.9)
        roi = roi[10:h-10, 10:w-10]
        M = cv2.getRotationMatrix2D((self.x, self.y), 45, 1.0)
        rotated = cv2.warpAffine(self.logo, M, (w, h))
        rotated = rotated[10:h-10, 10:w-10]
        # fill the empty corners after rotation to white
        blank = np.zeros(rotated.shape[:3],
                        dtype='uint8')
        blank += rotated
        roi[np.where(blank,False,True)] = 0
        cv2.imshow("Rotated by 45 Degrees", blank)
        # reshape rotated image 2d matrix to 3d
        # remove roi background to transparent
        print(rotated.shape)
        roi += blank
        roi = cv2.addWeighted(roi, .5, blank, .5, 1)
        
        
    def find_templates(self,framed_logo, sensitivity=0.9):

        template = framed_logo
        h, w = template.shape[:2]

        print('h', h, 'w', w)

        method = cv2.TM_CCORR_NORMED

        threshold = 0.90
        
        try:
            res = cv2.matchTemplate(self.logo, template, method)
        except:
            for i in range(5):
                time.sleep(1)
                res = cv2.matchTemplate(self.logo, template, method)
        res_h, res_w = res.shape[:2]

        # fake out max_val for first run through loop
        max_val = 1
        centers = []
        while max_val > sensitivity:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            centers.append( (max_loc[0] + w//2, max_loc[1] + h//2) )

            x1 = max(max_loc[0] - w//2, 0)
            y1 = max(max_loc[1] - h//2, 0)

            x2 = min(max_loc[0] + w//2, res_w)
            y2 = min(max_loc[1] + h//2, res_h)

            res[y1:y2, x1:x2] = 0
        mean_x = int(np.mean([x for x, y in centers]))
        mean_y = int(np.mean([y for x, y in centers]))
        # cv2.circle(template, (mean_x,mean_y), 7, (0, 0, 255), -1)
        cv2.imwrite('res.png', template)
        return (mean_x, mean_y)

    


    def update_position(self, mask,image):
        height, width = mask.shape
        # set self.size to match the size of the mask
        self.size = height
        np_shape_display = mask[[18]]
        points = np.array(np_shape_display, dtype=np.int32)
        self.rotation_radius = self.fit(points)
        print(self.rotation_radius)
        for (x,y) in points:
            self.x = x
            self.y = y


# background_subtractor = cv2.createBackgroundSubtractorMOG2()
# This will create an object