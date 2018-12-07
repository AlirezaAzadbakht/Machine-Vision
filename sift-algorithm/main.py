import ScaleSpace as scale_space
import ImageIO as io
import LoG as log
import findingKeyPoint as key_point
import gettingRideOfLowContrastKeypoints as decrese_keypoints
import KeypointOrientations as key_orientation
import GenerateFeature as gn


img = io.getImage("test2.jpg")

octaves = scale_space.getOctaves(img)

log_approximations = log.getDoGOctaves(octaves)

points = key_point.findPoints(octaves)

points = decrese_keypoints.removeEdge(points, octaves)

oriented_points = key_orientation.orientations(points, octaves)

final_points = gn.generate_feature(oriented_points, points, octaves)
