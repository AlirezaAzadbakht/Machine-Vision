# Bag of Visual Words

in this project we follow the steps in wikipedia and towarddatascience post about BoVW

toward data scinece post about BoVW is not compleme and correct we just use it to get the main idea
https://towardsdatascience.com/bag-of-visual-words-in-a-nutshell-9ceea97ce0fb

https://en.wikipedia.org/wiki/Bag-of-words_model_in_computer_vision

this project contains 3 class :

	Trainer
	Methods
	Tester

both tester and trainer class use same methodss so we made Methods class for easier use 


# Trainer Steps:

this implementation follows these simple steps :

## 1 . Getting descriptor
with the help of sift algorithm we get all the images in **Caltech  101_ObjectCategories** and save them in a list
 ```Python
 descriptor_list = []  
    images = []  
    labels = []  
    for filename1 in glob.glob('101_ObjectCategories/*'):  
      	for filename in glob.glob(filename1 + '/train/*.jpg'):  
     		 im = cv2.imread(filename)  
     		 labels.append(filename1[21:])  
     		 images.append(im)  
     		 image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  
     		 keypoint, descriptor = m.features(image, extractor)  
     		 for i in descriptor:  
    			  descriptor_list.append(i)
  ```

    

## 2. Run Kmeans clustering on descriptor list

as the steps in wikipedia said we use kmeans clustering algorihm and use the cluster centers in next step where we use them to create histogram of images 
 ```Python
 kmeans = KMeans(n_clusters=ClusterNumber)  
    kmeans.fit(descriptor_list)
  ```
    

## 3. make our visual word Bag
now we get the image's descriptor again and compare to the cluster centers that we computed in last step and for each descriptor we plus the value of the nearest cluster center
  ```Python
 histograms = []  
    for im in images:  
      histograms.append(m.get_histogram(kmeans.cluster_centers_, im))
  ```
    
get histogram method:
```Python
     def get_histogram(centers, image):  
      histogram = [0] * ClusterNumber  
        im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
      keypoint, descriptor = features(im, extractor)  
      for des in descriptor:  
      min = float('inf')  
      wherei = 0  
      i = 0  
      for cen in centers:  
      temp = distance(des, cen)  
      if temp < min:  
      min = temp  
                    wherei = i  
                i += 1  
      histogram[wherei] += 1  
      return histogram
  ```




 **now we are Done here we have our Bag of Visual Words for our dataset and we save it with pickle lib for future works** 


# Tester 

now the main job here is  we get an image to the findTopNearest method 
then it returns top N closest words to it
and we can compare them with the real label  
```Python
 def findTopNearest(histograms, targetHistogram, labels, top):  
      distances = []  
      for his in histograms:  
      distances.append(distance(his, targetHistogram))  
      arr = np.array(distances)  
      topIndex = (-arr).argsort()[-top:][::-1]  
      topLabels = []  
      for i in topIndex:  
      topLabels.append(labels[i])  
      return topLabels

  ```
    



# Results
we test our BoVW implemintaint in two ways:

if the top result for test image be the same as real label its true the result was  **folan %** correct 

if the result set have more than the half of true labels its true the result was **folan %** correct
