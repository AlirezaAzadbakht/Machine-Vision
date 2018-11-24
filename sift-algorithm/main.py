import ScaleSpace as scale_space
import ImageIO as io
import LoG as log

octaves = scale_space.getOctaves()

for li in octaves:
    for x in li:
        io.showImage(x)
        print(x)

log.calculateLoG(octaves)
