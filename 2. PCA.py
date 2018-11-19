import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Eating, exercise habbit and their body shape
df = pd.DataFrame(columns=['calory', 'breakfast', 'lunch', 'dinner', 'exercise', 'body_shape'])

df.loc[0] = [1200, 1, 0, 0, 2, 'Skinny']
df.loc[1] = [2800, 1, 1, 1, 1, 'Normal']
df.loc[2] = [3500, 2, 2, 1, 0, 'Fat']
df.loc[3] = [1400, 0, 1, 0, 3, 'Skinny']
df.loc[4] = [5000, 2, 2, 2, 0, 'Fat']
df.loc[5] = [1300, 0, 0, 1, 2, 'Skinny']
df.loc[6] = [3000, 1, 0, 1, 1, 'Normal']
df.loc[7] = [4000, 2, 2, 2, 0, 'Fat']
df.loc[8] = [2600, 0, 2, 0, 0, 'Normal']
df.loc[9] = [3000, 1, 2, 1, 1, 'Fat']

print(df.head(10))
# X is feature vectors
X = df[['calory', 'breakfast', 'lunch', 'dinner', 'exercise']]
print(X.head(9))

#Y is labels
Y = df[['body_shape']]
print(Y.head(10))

x_std = StandardScaler().fit_transform(X)
print(x_std)

#Coveriance Matrix of features
features = x_std.T
covariance_matrix = np.cov(features)
print(covariance_matrix)

eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)

projected_X = x_std.dot(eig_vecs.T[0])
print(projected_X)

result = pd.DataFrame(projected_X, columns=['PC1'])
result['Y-axis'] = 0.0
result['label'] = Y
print(result.head(10))

sns.Implot('PC1', 'y-axis', data=result, fit_reg=False, #x-axis, y-axis, data, no line
           scatter_kws={"s": 50},
           hue="label") # color

#title
plt.title('PCA result')