import ScaleSpace as scale_space
DoGOctaves = scale_space.getOctaves()

KeypointsOctaves=[]

for list in DoGOctaves:
    nextgenlist=[]
    for i in range(2):
        a = list[i]
        b = list[i + 1]
        c = list[i + 2]
        result = b
        height, width = b.shape[:2]
        for jj in range(width):

                for kk in range(height) :
                    target = b[jj][kk]
                    list[]

                    for i in range(3):
                        for j in range(3):
                            try:
                                list.append(a[jj-1 +i][kk-1 +jw])

                    for i in range(3):
                        for j in range(3):
                            try:
                                if i != 1 and j!= 1:
                                    list.append(b[jj - 1 + i][kk - 1 + j])


                    for i in range(3):
                        for j in range(3):
                            try:
                                list.append(c[jj - 1 + i][kk - 1 + j])


                    tmax = max(list)
                    tmin = min(list)
                    if target > tmax:
                        result[jj][kk] = target
                    else if target < tmin:
                        result[jj][kk] = target
                    else:
                        result[jj][kk] = 0

        nextgenlist.append(result)
    KeypointsOctaves.append(nextgenlist)
    
