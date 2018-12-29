import pickle
import glob
import cv2
import Methods as m

histograms = []
labels = []
centers = []

with open("histograms.txt", "rb") as fp:  # Unpickling
    histograms = pickle.load(fp)

with open("labels.txt", "rb") as fp:  # Unpickling
    labels = pickle.load(fp)

with open("centers.txt", "rb") as fp:  # Unpickling
    centers = pickle.load(fp)

print(len(histograms) , len(labels) , len(centers))

images = []
trainLabels = []
for filename1 in glob.glob('101_ObjectCategories/*'):
    for filename in glob.glob(filename1 + '/test/*.jpg'):
        im = cv2.imread(filename)
        trainLabels.append(filename1[21:])
        images.append(im)

cTrue=0
c=0;
for i in range(len(images)):
    c+=1
    h = m.get_histogram(centers, images[i])
    topLabels = m.findTopNearest(histograms, h, labels, 5)
    print("Bag Of Word result :", topLabels)
    print("real Label :", labels[i])
    if(labels[i] == topLabels[0]):
        cTrue +=1
        print("true")
    else:
        print("false")
    print("-------------------------")

print(float(float(cTrue)*100/float(c)))


