# Bag of Visual Words


 ![alt text](http://people.csail.mit.edu/fergus/iccv2005/bagofwords.gif)


in this project, we follow the steps in Wikipedia and toward data science post about BoVW

toward data science post about BoVW is not complete and correct we just use it to get the main idea

https://towardsdatascience.com/bag-of-visual-words-in-a-nutshell-9ceea97ce0fb


https://en.wikipedia.org/wiki/Bag-of-words_model_in_computer_vision

this project contains 3 class :

	Trainer
	Methods
	Tester

both tester and trainer class use the same methods so we made Methods class for easier use 

# dataset :
![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Bag-of-Visual-Words/101_ObjectCategories/airplanes/test/image_0006.jpg)
![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Bag-of-Visual-Words/101_ObjectCategories/anchor/test/image_0008.jpg)
![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Bag-of-Visual-Words/101_ObjectCategories/bass/test/image_0009.jpg)
![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Bag-of-Visual-Words/101_ObjectCategories/barrel/test/image_0006.jpg)
![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Bag-of-Visual-Words/101_ObjectCategories/ant/test/image_0006.jpg)

# Trainer Steps:

this implementation follows these simple steps :

## 1 . Getting descriptor
with the help of sift algorithm we get all the images in **Caltech  101_ObjectCategories** and save them in a list
 ```Python
 for filename1 in glob.glob('101_ObjectCategories/*'):
    for filename in glob.glob(filename1 + '/*.jpg'):
        im = cv2.imread(filename)
        labels.append(filename1[21:])
        images.append(im)
        image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        keypoint, descriptor = m.features(image, extractor)
        for i in descriptor:
            descriptor_list.append(i)
 ```

    

## 2. executing K-means clustering on descriptor list

as the steps in Wikipedia said we use K-means clustering algorithm and use the cluster centers in the next step where we use them to create a histogram of images 
 ```Python
 kmeans = KMeans(n_clusters=ClusterNumber)
 kmeans.fit(descriptor_list)
 ```
    

## 3. make our visual word Bag
now we get the image's descriptor again and compare to the cluster centers that we computed in the last step and for each descriptor we plus the value of the nearest cluster center with Euclidean distance
  ```Python
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

for k = 50 in Kmeans:

if the top result for test image be the same as real label its true the result was  **24 %** correct

for k = 150 in Kmeans:

if the top result for test image be the same as real label its true the result was  **24 %** correct




the reason we get this result is we use 50 centers in Kmeans and it is not enough to cover dataset 

it is obvious if we increase centers it took more time to learn and get better results

console output :

```
Bag Of Word result : ['airplanes', 'airplanes', 'bass', 'barrel', 'ant']
real Label : airplanes
true
-------------------------
Bag Of Word result : ['airplanes', 'bass', 'airplanes', 'ant', 'barrel']
real Label : airplanes
true
-------------------------
Bag Of Word result : ['bass', 'bass', 'ant', 'airplanes', 'airplanes']
real Label : airplanes
false
-------------------------
Bag Of Word result : ['airplanes', 'airplanes', 'barrel', 'ant', 'bass']
real Label : airplanes
true
-------------------------
Bag Of Word result : ['bass', 'airplanes', 'barrel', 'anchor', 'ant']
real Label : airplanes
false
-------------------------
Bag Of Word result : ['bass', 'ant', 'bass', 'airplanes', 'airplanes']
real Label : anchor
false
-------------------------
Bag Of Word result : ['barrel', 'airplanes', 'barrel', 'airplanes', 'airplanes']
real Label : anchor
false
-------------------------
Bag Of Word result : ['anchor', 'barrel', 'bass', 'airplanes', 'anchor']
real Label : anchor
true
-------------------------
Bag Of Word result : ['ant', 'barrel', 'airplanes', 'ant', 'airplanes']
real Label : anchor
false
-------------------------
Bag Of Word result : ['airplanes', 'airplanes', 'bass', 'barrel', 'airplanes']
real Label : anchor
false
-------------------------
Bag Of Word result : ['ant', 'barrel', 'airplanes', 'ant', 'airplanes']
real Label : ant
true
-------------------------
Bag Of Word result : ['ant', 'airplanes', 'airplanes', 'ant', 'anchor']
real Label : ant
true
-------------------------
Bag Of Word result : ['anchor', 'airplanes', 'barrel', 'barrel', 'bass']
real Label : ant
false
-------------------------
Bag Of Word result : ['bass', 'ant', 'airplanes', 'airplanes', 'ant']
real Label : ant
false
-------------------------
Bag Of Word result : ['airplanes', 'anchor', 'barrel', 'bass', 'anchor']
real Label : ant
false
-------------------------
Bag Of Word result : ['airplanes', 'bass', 'bass', 'airplanes', 'ant']
real Label : barrel
false
-------------------------
Bag Of Word result : ['airplanes', 'ant', 'bass', 'bass', 'ant']
real Label : barrel
false
-------------------------
Bag Of Word result : ['bass', 'ant', 'airplanes', 'bass', 'airplanes']
real Label : barrel
false
-------------------------
Bag Of Word result : ['ant', 'airplanes', 'bass', 'anchor', 'barrel']
real Label : barrel
false
-------------------------
Bag Of Word result : ['ant', 'barrel', 'airplanes', 'ant', 'barrel']
real Label : barrel
false
-------------------------
Bag Of Word result : ['ant', 'bass', 'airplanes', 'anchor', 'bass']
real Label : bass
false
-------------------------
Bag Of Word result : ['ant', 'airplanes', 'airplanes', 'barrel', 'bass']
real Label : bass
false
-------------------------
Bag Of Word result : ['ant', 'ant', 'bass', 'airplanes', 'airplanes']
real Label : bass
false
-------------------------
Bag Of Word result : ['ant', 'bass', 'airplanes', 'anchor', 'airplanes']
real Label : bass
false
-------------------------
Bag Of Word result : ['airplanes', 'bass', 'barrel', 'bass', 'ant']
real Label : bass
false
-------------------------
24.0
```

fun fact: when we increase k size the algorithm confuse and labels all the airplanes a bass :) 
