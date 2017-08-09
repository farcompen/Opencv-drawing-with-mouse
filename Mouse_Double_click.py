#! /usr/bin python
# -*- coding:utf-8 -*-



import cv2


def daire_ciz(event, x, y, flags, param):
    global onceki_x, onceki_y
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(resim, (x, y), 50, (255, 0, 0), 1)
        onceki_x, onceki_y = x, y


    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(resim, (onceki_x, onceki_y), (x, y), (0, 255, 0), 1)

resim = cv2.imread('dybala.jpg', 1)
cv2.namedWindow('resim')
cv2.setMouseCallback('resim', daire_ciz)
while True:
    cv2.imshow('resim', resim)
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
#ssss
