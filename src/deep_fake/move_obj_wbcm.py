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
img = "C:\\Users\\mahta\\OneDrive\\Documents\\GitHub\\autism_Robot\\src\\deep_fake\\logo.png"
# Object class to insert logo
class Object:
    def __init__(self, start_x=100, start_y=100, size=50):
        self.logo_org = cv2.imread(img)
        self.size = size
        self.logo = cv2.resize(self.logo_org, (size, size))
        self.img2gray = cv2.cvtColor(self.logo, cv2.COLOR_BGR2GRAY)
        # Converting image to a binary image 
        # ( black and white only image).  
        _, logo_mask = cv2.threshold(self.img2gray, 1, 255, cv2.THRESH_BINARY)
        self.logo_mask = logo_mask
        self.on_mask = False
        self.coordinates = self.extract_edges()
        self.x = self.coordinates[0]
        self.y = self.coordinates[1]

        

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
            cv2.drawContours(img2, [approx], 0, (0, 0, 255), 2) 

            # Used to flatted the array containing 
            # the co-ordinates of the vertices. 
            M = cv2.moments(cnt)
            if M['m00'] != 0:
                self.cx = int(M['m10']/M['m00'])
                self.cy = int(M['m01']/M['m00'])
                cv2.circle(self.logo, (self.cx, self.cy), 7, (0, 0, 255), -1)
            
            print(self.cx,self.cy)
            n = approx.ravel() 
            i = 0

            for j in n : 
                if(i % 2 == 0): 
                    x = n[i] 
                    y = n[i + 1] 
                    coordinates.append((x,y))

        return (self.cx,self.cy)


    def insert_object(self, frame):
        roi = frame[self.y:self.y + self.size, self.x:self.x + self.size]
        roi[np.where(self.logo_mask)] = 0
        roi += self.logo
        roi = cv2.addWeighted(roi, .5, self.logo, .5, 1)

    def find_templates(self , sensitivity=0.5):

        template = cv2.imread(img, cv2.IMREAD_COLOR)
        
        self.logo_org = template
        h, w = template.shape[:2]

        print('h', h, 'w', w)

        method = cv2.TM_CCORR_NORMED

        threshold = 0.90

        res = cv2.matchTemplate(self.logo_mask, template, method)
        res_h, res_w = res.shape[:2]

        # fake out max_val for first run through loop
        max_val = 1
        centers = []
        while max_val > sensitivity:
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > sensitivity:
                centers.append( (max_loc[0] + w//2, max_loc[1] + h//2) )

                x1 = max(max_loc[0] - w//2, 0)
                y1 = max(max_loc[1] - h//2, 0)

                x2 = min(max_loc[0] + w//2, res_w)
                y2 = min(max_loc[1] + h//2, res_h)

                res[y1:y2, x1:x2] = 0

                image = cv2.rectangle(image,(max_loc[0],max_loc[1]), (max_loc[0]+w+1, max_loc[1]+h+1), (0,255,0) )

        print(centers)

        cv2.imwrite('output.png', image)

    find_templates("enemy_logo.png", 0.90)


    def update_position(self, mask,image):
        height, width = mask.shape
        np_shape_display = mask[[RIGHT_TOP_EYELID][0]]
        points = np.array(np_shape_display, dtype=np.int32)
        mapped_points = points
        print(self.x,self.y,points)
        cv2.imshow('blank',self.logo)
        for (x,y) in mapped_points:
            self.x = x
            self.y = y
        cv2.circle(image, (self.x, self.y), 7, (0, 0, 255), -1)

# background_subtractor = cv2.createBackgroundSubtractorMOG2()
# This will create an object