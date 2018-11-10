import ScaleSpace as a
import ImageIO as io
Oc =a.getOctaves()

for li in Oc:
    for x in li:
        io.showImage(x)