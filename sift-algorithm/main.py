import ScaleSpace as scale_space
import ImageIO as io
import LoG as log
import findingKeyPoint as key_point
import gettingRideOfLowContrastKeypoints as decrese_keypoints

img = io.getImage("test2.jpg")

octaves = scale_space.getOctaves(img)

log_approximations = log.getDoGOctaves(octaves)

points = key_point.findPoints(octaves)

points = decrese_keypoints.removeEdge(points, octaves)

# for i in enumerate(points):
#     for j in enumerate(i):
#         print(i + " :" + j )