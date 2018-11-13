import cv2

print('hello world')
def showImage(img):
    cv2.imshow('',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getImage(name):
    return cv2.imread(name, 0)
