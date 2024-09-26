import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)
images = np.array(X[:50]).reshape(-1, 28, 28)
labels = np.array(y[:50])

fig, axes = plt.subplots(5, 10, figsize=(10, 5))

for i, ax in enumerate(axes.flat):
    ax.imshow(images[i], cmap='BuPu')
    ax.axis('off')
    ax.text(0.5, -0.5, str(labels[i]), fontsize=12, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.show()
