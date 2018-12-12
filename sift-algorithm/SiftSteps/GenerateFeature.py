import numpy as np
import math
import cv2 as cv


def generate_feature(key_list, points, scale_spaces):
    mask_x = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    mask_y = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

    for index, scale_space in enumerate(scale_spaces):
        # height, width = scale_space.shape[:2]
        imX = cv.filter2D(scale_spaces[index][0], -1, kernel=np.array(mask_x))
        imY = cv.filter2D(scale_spaces[index][0], -1, kernel=np.array(mask_y))
        imX = np.lib.pad(np.array(imX), ((8, 8), (8, 8)), 'symmetric')
        imY = np.lib.pad(np.array(imY), ((8, 8), (8, 8)), 'symmetric')
        featrure = []

        for i in key_list[index]:
            featrue_points = []
            first = i[0]
            second = i[1]
            for j in range(-2, 2):
                first_1 = first + j * 4
                for k in range(-2, 2):
                    second_1 = second + k * 4
                    orients = np.zeros(8)

                    for n in range(4):
                        for m in range(4):
                            if imX[first - first_1 + n][second - second_1 + m] == 0:
                                tetha = 0
                            else:
                                tetha = imY[first - first_1 + n][second - second_1 + m] / (
                                    imX[first - first_1 + n][second - second_1 + m])

                            for l, degree in enumerate(range(1, 8)):
                                if ((degree - 1) / 4) * math.pi <= tetha < (degree / 4) * math.pi:
                                    orients[l] += 1

                    featrure.append(orients)
            featrue_points.append(featrure)
    return featrue_points
