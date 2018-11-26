import ScaleSpace as scale_space
import ImageIO as io
import LoG as log

octaves = scale_space.getOctaves()

test = log.getDoGOctaves(octaves)
for octaves in test:
	for i in octaves:
		io.showImage(i)