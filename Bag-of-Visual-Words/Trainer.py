# pip install opencv-python==3.3.0.10 opencv-contrib-python==3.3.0.10 pip install -U scikit-learn
import glob
import cv2
from sklearn.cluster import KMeans
import pickle
import Methods as m


extractor = m.extractor
ClusterNumber = m.ClusterNumber


print("~ getting descriptor..")
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
print("~ Kmeans Clustering..")
print("~~ descriptor size :", len(descriptor_list))
kmeans = KMeans(n_clusters=ClusterNumber)
kmeans.fit(descriptor_list)
print("~~ cluster center size :", len(kmeans.cluster_centers_))
print("~ getting histograms..")
histograms = []
for im in images:
    histograms.append(m.get_histogram(kmeans.cluster_centers_, im))

with open("histograms.txt", "wb") as fp:
    pickle.dump(histograms, fp)

with open("labels.txt", "wb") as fp:
    pickle.dump(labels, fp)

with open("centers.txt", "wb") as fp:
    pickle.dump(kmeans.cluster_centers_, fp)

print("~ saved.")

