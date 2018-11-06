from sklearn.datasets import load_iris
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

iris = load_iris()
data, target = load_iris().data, load_iris().target

x = data[:, 0:2]
y = target

# a
plt.hist2d(x=x[:, 0], y=x[:, 1])
plt.colorbar()
plt.title('4-a')

# b
fig = plt.figure()
axb = fig.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(x[:, 0], x[:, 1])
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
dz = hist.flatten()
axb.bar3d(xpos, ypos, 0, 0.5, 0.5, dz)
plt.title('4-b')

# c
fig = plt.figure()
axc = fig.add_subplot(111, projection='3d')
axc.scatter(xpos, ypos, dz)
plt.title('4-c')

