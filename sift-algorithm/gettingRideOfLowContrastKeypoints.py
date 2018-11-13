import ScaleSpace as scale_space
KeypointsOctaves = scale_space.getOctaves()
lowTershold = 50
for list in KeypointsOctaves:
    for a in list:
        result = a
        height, width = b.shape[:2]
        for j in range(width):
            for k in range(height):
                if a[j][k] < lowTershold:
                    result[j][k] = 0
