from fcmeans import FCM
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt
from seaborn import scatterplot as scatter
import pandas as pd


# create artifitial dataset
n_samples = pd.read_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Categorized Data\Skills\test.csv')
n_bins = 3  # use 3 bins for calibration_curve as we have 3 clusters here
centers = [(6, 11, 16), (25, 25, 25), (0, 0, 0)]

X,_ = make_blobs(n_samples=550, n_features=3, cluster_std=1.0,
                  centers=centers, shuffle=False, random_state=42)

# fit the fuzzy-c-means
fcm = FCM(n_clusters=3)
fcm.fit(X)

# outputs
fcm_centers = fcm.centers
fcm_labels  = fcm.u.argmax(axis=1)


# plot result
#%matplotlib inline
f, axes = plt.subplots(1, 2, figsize=(11,5))
scatter(X[:,0], X[:,1], ax=axes[0])
scatter(X[:,0], X[:,1], ax=axes[1], hue=fcm_labels)
scatter(fcm_centers[:,0], fcm_centers[:,1], ax=axes[1],marker="s",s=200)
plt.show()