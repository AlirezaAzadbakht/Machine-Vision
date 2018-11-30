import cv2
import ImageIO as io
import math


def getOctaves():
    img = io.getImage("test2.jpg")
    Octaves = []
    b = 0.5
    # print(b)
    for x in range(4):
        List = []
        a = b
        # print(a)
        for y in range(5):
            a = a * math.sqrt(2)
            List.append(cv2.GaussianBlur(img, (5, 5), a))
            io.showImage(List[y])
        b *= 2
        Octaves.append(List)
        height, width = img.shape[:2]
        img = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_AREA)
    return Octaves
