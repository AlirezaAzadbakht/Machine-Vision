from SiftSteps import LoG, ScaleSpace as scale_space, findingKeyPoint as key_point, \
    gettingRideOfLowContrastKeypoints as decrese_keypoints, GenerateFeature as gn, \
    KeypointOrientations as key_orientation
import ImageIO as io

img = io.getImage("test2.jpg")

octaves = scale_space.getOctaves(img)

log_approximations = LoG.getDoGOctaves(octaves)

points = key_point.findPoints(octaves)

points = decrese_keypoints.removeEdge(points, octaves)

oriented_points = key_orientation.orientations(points, octaves)

final_points = gn.generate_feature(oriented_points, points, octaves)
