First of all in this project , we try to implement scale-invariant feature transform (SIFT) a feature detection algorithm .


# structure
 SiftSteps module contains six file , each step implement in of file then all of them import in main.py .
 
 ## The scale space
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
        
`getOctaves` in ScaleSpace makes octaves and scales needed
 
 



