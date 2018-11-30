# import ScaleSpace as scale_space
# DoGOctaves = scale_space.getOctaves()

KeypointsOctaves = []

def findPoints(poinsts):
    for dog_octaves in poinsts:
        nextgenlist=[]
        for sacle in range(2):
            a = dog_octaves[sacle]
            b = dog_octaves[sacle + 1]
            c = dog_octaves[sacle + 2]
            result = b
            height, width = b.shape[:2]
            print(width, height)
            for jj in range(height):
                for kk in range(width):
                    # print(jj, kk)
                    target = b[jj][kk]
                    window = []
                    for i in range(3):
                        for j in range(3):
                            try:
                                window.append(a[jj-1 +i][kk-1 +j])
                            except:
                                print('error1')
                    for i in range(3):
                        for j in range(3):
                            try:
                                if i != 1 and j!= 1:
                                    window.append(b[jj - 1 + i][kk - 1 + j])
                            except:
                                print('error2')
                    for i in range(3):
                        for j in range(3):
                            try:
                                window.append(c[jj - 1 + i][kk - 1 + j])
                            except:
                                print('error3')
                    tmax = max(window)
                    tmin = min(window)
                    if target > tmax:
                        result[jj][kk] = target
                    elif target < tmin:
                        result[jj][kk] = target
                    else:
                        result[jj][kk] = 0
            nextgenlist.append(result)
        KeypointsOctaves.append(nextgenlist)
    return KeypointsOctaves
    
