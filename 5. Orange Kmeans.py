import orange

import random
random.seed(42)

iris = Orange.data.Table("iris")
km = Orange.clustering.kmeans.Clustering(iris, 3)
print(km.klusters[10:])