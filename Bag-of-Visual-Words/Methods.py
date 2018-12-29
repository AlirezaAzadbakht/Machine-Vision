import numpy as np
import cv2

extractor = cv2.xfeatures2d.SIFT_create()
ClusterNumber = 150


def features(image, extractor):
    keypoints, descriptors = extractor.detectAndCompute(image, None)
    return keypoints, descriptors


def get_histogram(centers, image):
    histogram = [0] * ClusterNumber
    im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    keypoint, descriptor = features(im, extractor)
    for des in descriptor:
        min = float('inf')
        wherei = 0
        i = 0
        for cen in centers:
            temp = distance(des, cen)
            if temp < min:
                min = temp
                wherei = i
            i += 1
        histogram[wherei] += 1
    return histogram


def distance(a, b):
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i]) * (a[i] - b[i])
    return sum


def findTopNearest(histograms, targetHistogram, labels, top):
    distances = []
    for his in histograms:
        distances.append(distance(his, targetHistogram))
    arr = np.array(distances)
    topIndex = (-arr).argsort()[-top:][::-1]
    topLabels = []
    for i in topIndex:
        topLabels.append(labels[i])
    return topLabels
