import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

X, y = load_iris(return_X_y=True)
species_names = ['Setosa', 'Versicolour', 'Virginica']
x_feature = X[:, 0]
y_feature = X[:, 1]
size_feature = X[:, 3]

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x_feature, y_feature, c=y, s=size_feature * 100, cmap='Dark2', alpha=0.7)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Iris Dataset Scatter Plot')
handles, colors = scatter.legend_elements(prop="colors", alpha=0.6)
plt.legend(handles, species_names, title="Species")

plt.show()
