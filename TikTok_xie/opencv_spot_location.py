import cv2
import cv2  as cv
import numpy as np
# def contours_info(image):
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#     contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     # 转灰度，二值化，寻找轮廓，返回轮廓信息
#     return contours
#
# def calculate_distance_():
#     img = cv.imread('pic_slide/big_pic.jpg')
#     template = cv.imread('pic_slide/slider_pic.jpg')
#     cv.imshow("input1", img)
#     cv.imshow("input2", template)
#
#     # 从函数那获取轮廓信息
#     contours_img = contours_info(img)
#     contours_template = contours_info(template)
#
#     # 几何矩计算后进行hu矩计算
#     mm2 = cv.moments(contours_template[0])
#     hum2 = cv.HuMoments(mm2)


# def calculate_distance():
#     img = cv2.imread('pic_slide/big_pic.jpg')
#     template = cv2.imread('pic_slide/slider_pic.jpg')
#
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色转灰度
#     template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)  # 彩色转灰度
#     # cv2.imshow("imgray", img_gray)
#
#     ret_img,dst_img = cv2.threshold(img_gray,55,255,cv2.THRESH_BINARY)
#     ret_template,dst_template = cv2.threshold(template_gray,55,255,cv2.THRESH_BINARY)
#
#     res = cv2.matchTemplate(dst_img,dst_template,cv2.TM_SQDIFF_NORMED)
#     cv2.normalize(res, res, 0, 1, cv2.NORM_MINMAX, -1)
#
#     min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
#     # print(max_loc)
#     print(min_loc)
#     return min_loc[0]
# calculate_distance()
# def calculate_distance():
#     img = cv2.imread('pic_slide/big_pic.jpg')
#     cv2.imshow('src',img)
#     cv2.waitKey()

# 读取图片
def ReadImg():
    img = cv2.imread('pic_slide/temp.jpg',1)
    cv2.imshow('src',img)
    return img

# 高斯滤波
def GausBlur(src):
    dst = cv2.GaussianBlur(src,(5,5),1.5)
    cv2.imshow('GausBlur',dst)
    return dst

# 灰度处理
def Gray_img(src):
    gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)

    return gray

# 二值化
def threshold_img(src):
    ret , binary = cv2.threshold(src,0,255,cv2.THRESH_BINARY|cv2.THRESH_TRIANGLE)
    print('threshold value %s'%ret)
    # binary = cv2.bitwise_not(binary)
    cv2.imshow('threshold',binary)
    return binary

# 开运算操作
def open_mor(src):
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(src,cv2.MORPH_OPEN,kernel,iterations=3)  # iterations进行3次操作
    cv2.imshow('open',opening)
    return opening

# 轮廓拟合
def draw_shape(open_img, gray_img):
    contours,hierarchy = cv2.findContours(open_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print('一共有%d个轮廓'%len(contours))

    # cnt = contours[0] # 得到第一个的轮廓
    for cnt in contours:
        # 计算当前轮廓的周长
        perimeter = cv2.arcLength(cnt, True)
        area  = cv2.contourArea(cnt)
        # print('perimeter:', perimeter)

        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        # cv2.drawContours(gray_img,[box],-1,(0,0,255),3)  # 画矩形框

        # 图像轮廓及中心点坐标
        M = cv2.moments(cnt)
        center_x = int(M['m10']/M['m00'])
        center_y = int(M['m01']/M['m00'])

        # if perimeter>=340 and perimeter<=350:
        if perimeter>=285 and perimeter<=375 and area >=1100  and area<=4000:
            print('perimeter=', perimeter)
            print('area=', area)
            print('center_x:', center_x)
            print('center_y:', center_y)
            print('--------------------------------------------------------')
            # cv2.drawContours(gray_img, [box], -1, (0, 0, 255), 3)  # 画矩形框
            cv2.circle(gray_img,(center_x,center_y),7,128,-1) # 绘制中心点
            str1 = '('+str(center_x)+','+str(center_y)+')'
            cv2.putText(gray_img,str1,(center_x-50,center_y+40),cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,255,0),2,cv2.LINE_AA)  # 绘制坐标点位
            cv2.imshow('show',gray_img)
        # return center_x
        # cv2.waitKey(0)

def main():
    src = ReadImg()
    gaus_img = GausBlur(src)
    gray_img = Gray_img(gaus_img)
    thres_img = threshold_img(gray_img)
    open_img = open_mor(thres_img)
    draw_shape(open_img,src)
    cv2.waitKey(0)

# src = ReadImg()
# gaus_img = GausBlur(src)
# gray_img = Gray_img(gaus_img)
# thres_img = threshold_img(gray_img)
# open_img = open_mor(thres_img)
# draw_shape(open_img,src)
main()



