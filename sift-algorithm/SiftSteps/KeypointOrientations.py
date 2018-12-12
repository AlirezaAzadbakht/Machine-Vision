import numpy as np
import cv2 as cv
import math
import ImageIO as io


def orientations(keypoints, scale_spaces):
    keypoints_list = []
    mask_x = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    mask_y = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    histogram = np.zeros(36)

    for i_index, octave in enumerate(keypoints):
        octave_list = []
        for j_index, scale_space in enumerate(octave):
            imX = cv.filter2D(scale_spaces[i_index][0], -1, kernel=np.array(mask_x))
            imY = cv.filter2D(scale_spaces[i_index][0], -1, kernel=np.array(mask_y))
            height, width = scale_space.shape[:2]
            # print('*** start')
            # print(height, width)
            # print('end ***')
            imX = np.lib.pad(np.array(imX), ((7, 7), (7, 7)), 'symmetric')
            imY = np.lib.pad(np.array(imY), ((7, 7), (7, 7)), 'symmetric')
            imX = np.array(imX).astype(np.int32)
            imY = np.array(imY).astype(np.int32)

            for jj in range(7, height):
                for kk in range(7, width):
                    if scale_space[jj][kk] != 0:
                        for n in range(-7, 8):
                            for m in range(-7, 8):
                                mag = math.sqrt((imX[jj + n + 1][kk] - imX[jj + n - 1][kk]) ** 2 +
                                                (imY[jj][kk + m + 1] - imY[jj][kk + m - 1]) ** 2)
                                if (imX[jj + n + 1][kk] - imX[jj + n - 1][kk]) == 0:
                                    theta = math.pi / 2
                                else:
                                    theta = math.atan((imY[jj][kk + m + 1] - imY[jj][kk + m - 1]) /
                                                      (imX[jj + n + 1][kk] - imX[jj + n - 1][kk]))

                                for index, i in enumerate(range(2, 74, 2)):
                                    if (i - 2) * (math.pi / 36) < theta <= i * (math.pi / 36):
                                        histogram[index] += theta * mag
                        max_hist = np.max(histogram)
                        peak = 0.8 * max_hist
                        for i in range(36):
                            if histogram[i] >= peak:
                                pair = [jj, kk, i * 100]
                                octave_list.append(pair)

        keypoints_list.append(octave_list)
    return keypoints_list
