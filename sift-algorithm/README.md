First of all in this project , we try to implement scale-invariant feature transform (SIFT) a feature detection algorithm .



 SiftSteps module contains six file , each step implement in of file then all of them import in` main.py` .
 `ImageIO.py` contains some functions for reading image with openCv .
 
 ##main
 
 in `main.py` we import all  steps of SIFT from SiftSteps.  
 
    img = io.getImage("test2.jpg")

    octaves = scale_space.getOctaves(img)

    log_approximations = LoG.getDoGOctaves(octaves)

    points = key_point.findPoints(octaves)

    points = decrese_keypoints.removeEdge(points, octaves)

    oriented_points = key_orientation.orientations(points, octaves)

    final_points = gn.generate_feature(oriented_points, points, octaves)

in first line we read image with `getImage` function in `ImageIO.py`. in the next line we call `getOctaves` function 
from `ScaleSpace.py` in SiftSteps module and pass image that read with `getImage` in it
 
 ### The scale space
 in first step we must make scale spaces of image, make four octave and each octave has 5 scale.
    
    def getOctaves(img):
        octaves = []
        b = 0.5
        # print(b)
        for x in range(4):
            List = []
            a = b
            for y in range(5):
                a = a * math.sqrt(2)
                List.append(cv2.GaussianBlur(img, (5, 5), a))
                io.showImage(List[y])
                
            b *= 2
            octaves.append(List)
            height, width = img.shape[:2]
            img = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_AREA)
        return octaves 
        
`getOctaves` in ScaleSpace makes octaves and scales needed and return a list with length of four so that each 
index of list is list that contain blurred with differents scales.
  
 
 



