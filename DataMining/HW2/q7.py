import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from tools import norm2_error


def train_error_on_KNN(k):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(x_train, y_train)

    y_pred_on_train = classifier.predict(x_train)

    err = norm2_error(y_train, y_pred_on_train)
    print('Error for {}NN classifier on train (euclidean distance): '.format(k), err)
    return err


dataset = pd.read_csv('US Presidential Data.csv')
x = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

errors = []
for k in range(1, 50):
    errors.append(train_error_on_KNN(k))

plt.plot(errors)
plt.show()
