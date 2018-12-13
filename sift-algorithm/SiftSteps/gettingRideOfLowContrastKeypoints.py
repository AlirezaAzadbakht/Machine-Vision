import ImageIO as io
import numpy as np
import cv2 as cv

keypoints = []
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


