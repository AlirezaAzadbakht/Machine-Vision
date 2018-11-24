import cv2
import ImageIO as io
import math


def getOctaves():
    img = io.getImage("test2.jpg")
    Octaves = []
    io.showImage(img)
    b = 1 / 2
    for x in range(4):
        List = []
        a = b
        for y in range(5):
            a = a * math.sqrt(2)
            List.append(cv2.GaussianBlur(img, (5, 5), sigmaX=a, sigmaY=0, borderType=1))
        b *= 2
        Octaves.append(List)
        height, width = img.shape[:2]
        img = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_AREA)
    return Octaves
