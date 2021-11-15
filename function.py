import pygame as pg
import cv2

# file = open("lol.txt","w")


def resize(Profile_pic):
    pg.transform.scale(Profile_pic,(50,50))


def pic(path,wei,hei):
    image = cv2.imread(path)
    Profile_pic = pg.image.load(path)
    [h,w,d] = image.shape
    if h>w:
            ww = int(wei*(w/h))
            hh = hei
            jj = int((wei-(wei*w/h))/2)
            kk = 0
    if w>h:
        ww = wei
        hh = int(hei*(h/w))
        jj = 0
        kk = int((hei-(hei*h/w))/2)
    return [ww,hh,jj,kk,Profile_pic]
