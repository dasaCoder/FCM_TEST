import skfuzzy as fuzz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['legend.fontsize'] = 15
plt.rcParams['figure.titlesize'] = 20
plt.rcParams['figure.figsize'] = (8,7)

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

# Define three cluster centers
centers = [[1, 1, 1, 11, 17, 16, 1, 16, 1, 1, 16, 8],
           [3, 3, 26, 5, 21, 3, 5, 3, 3, 3, 3, 8],
           [1, 5, 10, 10, 10, 16, 16, 10, 15, 15, 16, 16]]

# Define three cluster sigmas in x and y, respectively
sigmas = [[0.8, 0.8, 0.8, 1, 0.6, 0.9, 0.8, 0.9, 0.8, 0.8, 0.9, 0.7],
          [0.5, 0.5, 1, 1, 0.3, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.3],
          [0.3, 0.8, 0.3, 0.3, 0.3, 0.2, 0.8, 0.3, 0.7, 0.7, 0.2, 0.2]]

# Generate test data

df = pd.read_csv(r'../dataset/dataset.csv', names=['cat1', 'cat2' , 'cat3',  'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9','cat10', 'cat11', 'cat12'])

xpts = df.cat1
ypts = df.cat2
zpts = df.cat3
apts = df.cat4
bpts = df.cat5
cpts = df.cat6
dpts = df.cat7
epts = df.cat8
fpts = df.cat9
gpts = df.cat10
hpts = df.cat11
ipts = df.cat12
labels = df.cat1

for i, ((xmu, ymu, zmu, amu, bmu, cmu, dmu, emu, fmu, gmu, hmu, imu), (xsigma, ysigma, zsigma, asigma, bsigma, csigma, dsigma, esigma, fsigma, gsigma, hsigma, isigma)) in enumerate(zip(centers, sigmas)):
    xpts = np.hstack((xpts, np.random.standard_normal(500) * xsigma + xmu))
    ypts = np.hstack((ypts, np.random.standard_normal(500) * ysigma + ymu))
    zpts = np.hstack((zpts, np.random.standard_normal(500) * zsigma + zmu))
    apts = np.hstack((apts, np.random.standard_normal(500) * asigma + amu))
    bpts = np.hstack((bpts, np.random.standard_normal(500) * bsigma + bmu))
    cpts = np.hstack((cpts, np.random.standard_normal(500) * csigma + cmu))
    dpts = np.hstack((dpts, np.random.standard_normal(500) * dsigma + dmu))
    epts = np.hstack((epts, np.random.standard_normal(500) * esigma + emu))
    fpts = np.hstack((fpts, np.random.standard_normal(500) * fsigma + fmu))
    gpts = np.hstack((gpts, np.random.standard_normal(500) * gsigma + gmu))
    ipts = np.hstack((ipts, np.random.standard_normal(500) * hsigma + hmu))
    hpts = np.hstack((hpts, np.random.standard_normal(500) * isigma + imu))
    labels = np.hstack((labels, np.ones(500) * i))

# Visualize the test data
fig0, ax0 = plt.subplots()
for label in range(3):
    ax0.plot(xpts[labels == label], ypts[labels == label], '.')
ax0.set_title('Test data: 200 points.')
#plt.show()

fig1, axes1 = plt.subplots(3, 3, figsize=(10, 10))
alldata = np.vstack((xpts, ypts))
fpcs = []

for ncenters, ax in enumerate(axes1.reshape(-1), 2):
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
        alldata, ncenters, 2, error=0.005, maxiter=1000, init=None)

    # Store fpc values for later
    fpcs.append(fpc)

    # Plot assigned clusters, for each data point in training set
    cluster_membership = np.argmax(u, axis=0)
    for j in range(ncenters):
        ax.plot(xpts[cluster_membership == j],
                ypts[cluster_membership == j],
                zpts[cluster_membership == j],
                apts[cluster_membership == j],
                bpts[cluster_membership == j],
                cpts[cluster_membership == j],
                dpts[cluster_membership == j],
                epts[cluster_membership == j],
                fpts[cluster_membership == j],
                gpts[cluster_membership == j],
                hpts[cluster_membership == j],
                ipts[cluster_membership == j],'.', color=colors[j])

    # Mark the center of each fuzzy cluster
    for pt in cntr:
        ax.plot(pt[0], pt[1], 'rs')

    ax.set_title('Centers = {0}; FPC = {1:.2f}'.format(ncenters, fpc), size=12)
    ax.axis('off')

fig1.tight_layout()

fig2, ax2 = plt.subplots()
ax2.plot(np.r_[2:11], fpcs, color='#731810')
ax2.set_title("How Number of Clusters Change FPC?")
ax2.set_xlabel("Number of centers")
ax2.set_ylabel("Fuzzy partition coefficient")
plt.show()
