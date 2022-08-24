import cv2
import cv2  as cv
import numpy as np

src = cv2.imread("pic_slide/big_pic.jpg", 1) # read input image
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # convert to grayscale
blur = cv2.blur(gray, (3, 3)) # blur the image
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
# thresh = cv2.bitwise_not(thresh)

kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=3)  # iterations进行3次操作
cv2.imshow('1',opening)
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# create hull array for convex hull points
hull = []

#calculate points for each contour
for i in range(len(contours)):
    #creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))

# create an empty black image
drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

# draw contours and hull points
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    cv2.drawContours(drawing, hull, i, color, 1, 8)
    cv2.imshow('2',drawing)
# for i in range(len(contours)):
#     cv2.drawContours(src,hull,-1,(0,0,255),3)  # 画矩形框
#     cv2.imshow('src',src)
cv2.waitKey(0)
