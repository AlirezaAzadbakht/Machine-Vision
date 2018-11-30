import ScaleSpace as scale_space
import ImageIO as io
import LoG as log
import findingKeyPoint as key_point


octaves = scale_space.getOctaves()

log_approximations = log.getDoGOctaves(octaves)

points = key_point.findPoints(octaves)

print(points)