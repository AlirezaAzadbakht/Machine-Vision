import cv2


def showImage(img):
    cv2.imshow('', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getImage(name):
    return cv2.imread(name, 0)


# def drawKeypoints(img, kp):
#     image = cv2.drawKeypoints(img, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     showImage(image)
