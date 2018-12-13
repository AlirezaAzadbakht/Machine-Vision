import ImageIO as io

DoGOctaves = []


def getDoGOctaves(octaves):
    print('LOG')
    counter = 0
    for list in octaves:
        nlist = []
        for i in range(4):

            a = list[i + 1]
            b = list[i]

            height, width = a.shape[:2]
            for k in range(width):
                for j in range(height):
                    if b[j][k] < a[j][k]:
                        b[j][k] = 0
                    else:
                        b[j][k] = b[j][k] - a[j][k]
                        if b[j][k] > 0:
                            counter += 1
                            # b[j][k] = 255

            nlist.append(b)
            # io.showImage(b)
            print(counter)

        DoGOctaves.append(nlist)
        # print(counter)

    return DoGOctaves
