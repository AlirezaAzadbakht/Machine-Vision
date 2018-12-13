import ImageIO as io
keypoints_octaves = []
def findPoints(poinsts):
    for dog_octaves in poinsts:
        nextgen_list = []
        for sacle in range(2):
            a = dog_octaves[sacle]
            b = dog_octaves[sacle + 1]
            c = dog_octaves[sacle + 2]
            result = b
            height, width = b.shape[:2]
            # print(width, height)
            for jj in range(height):
                for kk in range(width):
                    target = b[jj][kk]
                    window = []
                    for i in range(3):
                        for j in range(3):
                            try:
                                window.append(a[jj - 1 + i][kk - 1 + j])
                            except:
                                print('')
                    for i in range(3):
                        for j in range(3):
                            try:
                                if i != 1 and j != 1:
                                    window.append(b[jj - 1 + i][kk - 1 + j])
                            except:
                                print('')
                    for i in range(3):
                        for j in range(3):
                            try:
                                window.append(c[jj - 1 + i][kk - 1 + j])
                            except:
                                print('')
                    tmax = max(window)
                    tmin = min(window)
                    if target > tmax:
                        result[jj][kk] = target
                        # result[jj][kk] = 255
                    elif target < tmin:
                        result[jj][kk] = target
                        # result[jj][kk] = 255
                    else:
                        result[jj][kk] = 0
            print('how keypoints')
            io.showImage(result)
            nextgen_list.append(result)
        keypoints_octaves.append(nextgen_list)
    return keypoints_octaves
