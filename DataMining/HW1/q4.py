from sklearn.datasets import load_iris
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import pandas as pd

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

plt.show()

# d
print('\n\n===================== 4-d =====================\n')
print('Mean vector: ', np.mean(data, axis=0))
print('Variance vector: ', np.var(data, axis=0))

# e
print('\n\n===================== 4-e =====================\n')

print('Covariance Matrix :\n')
cov01 = np.cov(x[:, 0], x[:, 1])
print(cov01)

# f
print('\n\n===================== 4-f =====================\n')

print('Correlate Matrix :\n')
print(np.corrcoef(x[:, 0], x[:, 1]))

# g
print('\n\n===================== 4-g =====================\n')

df = pd.DataFrame()
df['f1'] = data[:, 0]
df['f2'] = data[:, 1]
df['f3'] = data[:, 2]
df['f4'] = data[:, 3]

corr = df.corr()
print(corr)
argmax = np.argmax(corr.values - np.identity(4))
print("\nfeature {} and feature {}".format(int(argmax/4)+1, argmax%4+1))

# h
print('\n\n===================== 4-g =====================\n')
c1 = np.corrcoef(y, data[:, 0])[0][1]
c2 = np.corrcoef(y, data[:, 1])[0][1]
c3 = np.corrcoef(y, data[:, 2])[0][1]
c4 = np.corrcoef(y, data[:, 3])[0][1]
print('best feature: ', np.argmax([c1, c2, c3, c4])+1)
