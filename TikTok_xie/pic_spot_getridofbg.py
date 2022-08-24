import time

import cv2 as cv
import numpy as np
import imutils

image = cv.imread("pic_slide/big_pic.jpg",cv.IMREAD_GRAYSCALE)
binary = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,25,15)
se = cv.getStructuringElement(cv.MORPH_RECT,(1,1))
se = cv.morphologyEx(se, cv.MORPH_CLOSE, (2,2))
mask = cv.dilate(binary,se)
cv.imshow("image",image)

mask1 = cv.bitwise_not(mask)
binary =cv.bitwise_and(image,mask)
result = cv.add(binary,mask1)
cv.imwrite('pic_slide/temp.jpg',result)

# 睡眠1s后，重新读取中间照片
time.sleep(1)
result = cv.imread('pic_slide/temp.jpg')
gray = cv.cvtColor(result,cv.COLOR_BGR2GRAY) # 灰度
blurred = cv.GaussianBlur(gray,(5,5),0)   # 5*5的内核高斯平滑
thresh = cv.threshold(blurred,108,255,cv.THRESH_BINARY)[1]   # 阈值化，阈值化后形状被表示成黑色背景上的白色前景
kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations=3)  # iterations进行3次操作
cv.imwrite('pic_slide/temp.jpg',opening)
cv.imshow('Image',opening)


cnts = cv.findContours(opening.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

print('cnts中的元素个数为：',len(cnts))
#  计算轮廓中心
for c in cnts:
    M = cv.moments(c)
    try:
        cX = int(M['m10']/M['m00'])
        cY = int(M['m01']/M['m00'])
    except Exception as e:
        print(e)

    # 在图像上绘制形状的轮廓和中心
    cv.drawContours(image,[c],-1,(0,255,0),2)
    cv.circle(image,(cX,cY),7,(255,255,255),-1)
    cv.putText(image,'center',(cX-20,cY-20),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
    cv.imshow('show', image)
    print('cX=',cX,'\n','cY=',cY)
    print('-----------------------')

cv.waitKey(0)

# cv.imshow("reslut",result)
# cv.imwrite("reslut00.jpg",result)
# cv.waitKey(0)
# cv.destroyAllWindows()