import ImageIO as io
import numpy as np
import cv2 as cv

keypoints = []


def removeLowThreshold(low_threshold, points):
    low_threshold_keypoints=[]
    for list in points:
        scales_list=[]
        for index, a in enumerate(list):
            print(index)
            result = a
            height, width = a.shape[:2]
            # avoid low_threshold pixels
            for j in range(height):
                for k in range(width):
                    if a[j][k] < low_threshold[index]:
                        result[j][k] = 0
                    else:
                        result[j][k] = 255
            low_threshold[index] *= 0.75
            io.showImage(result)
            scales_list.append(result)
        low_threshold_keypoints.append(scales_list)
    return low_threshold_keypoints



def removeEdge(points, scale_space):
    mask_x = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    mask_y = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    for a, list in enumerate(points):
        scale_list = []
        imX = cv.filter2D(scale_space[a][0], -1, kernel=np.array(mask_x))
        imY = cv.filter2D(scale_space[a][0], -1, kernel=np.array(mask_y))
        for index, item in enumerate(list):
            height, width = item.shape[:2]

            for j in range(height):
                for k in range(width):
                    if imX[j][k] != 0 and imY[j][k] != 0:
                        if 0.5 < imX[j][k] / imY[j][k] < 1.5 and item[j][k] != 0:
                            item[j][k] = 0
                    else:
                        item[j][k] = 0
            io.showImage(item)
            scale_list.append(item)
        keypoints.append(scale_list)
    return keypoints


def removeKeypoints(low_threshold, points, octaves):
    new_points = removeLowThreshold(low_threshold, points)
    key_points = removeEdge(new_points, octaves)
    return key_points
