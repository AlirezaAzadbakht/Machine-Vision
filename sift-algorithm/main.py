import ImageIO as io
from SiftSteps import LoG, \
    ScaleSpace as scale_space, \
    findingKeyPoint as key_point, \
    gettingRideOfLowContrastKeypoints as decrese_keypoints, \
    GenerateFeature as gn, \
    KeypointOrientations as key_orientation

img = io.getImage("test2.jpg")

octaves = scale_space.getOctaves(img)

log_approximations = LoG.getDoGOctaves(octaves)

points = key_point.findPoints(octaves)

points = decrese_keypoints.removeKeypoints([2, 4], points, octaves)

oriented_points = key_orientation.orientations(points, octaves)

final_points = gn.generate_feature(oriented_points, points, octaves)
