from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
from tools import extract_dataset, frange


class Linear_SVM_Classifier:
    def __init__(self, C):
        self.clf = svm.SVC(gamma='scale', kernel='linear', C=C)

    def train(self, features, labels_id):
        self.clf.fit(features, labels_id)

    def predict(self, features):
        return int(self.clf.predict(np.reshape(features, (1, -1)))[0])  # shape:(1, -1) -> one sample, some features

    def multi_predict(self, features):
        return self.clf.predict(features)  # shape:(-1, -1) -> some samples, some features


def build_classifier(train, C=1.):
    classifier = Linear_SVM_Classifier(C)
    classifier.train(train[:, 0:-1], train[:, -1])
    return classifier


def calculate_error(classifier, test):
    results = classifier.multi_predict(test[:, 0:-1])
    err_num = 0
    for i in range(len(results)):
        if results[i] != test[i, -1]:
            err_num += 1

    return err_num / len(results)


def plot_error_on_C(dataset_address='datasets/svmdata.csv'):
    train, test, validation = extract_dataset(dataset_address, need_validation=True)
    c_array = []
    err_array = []
    for c in frange(0.01, 1, 0.01):
        classifier = build_classifier(train, c)
        err_array.append(calculate_error(classifier, validation))
        c_array.append(c)
    plt.ylabel('Error (0-1)')
    plt.plot(c_array, err_array)
    plt.show()

    print('best C =', c_array[np.argmin(err_array)])


def plot_linear_svm(dataset_address='datasets/svmdata.csv', c=1.):
    train, test, validation = extract_dataset(dataset_address, need_validation=True)
    classifier = build_classifier(train, c)

    class0, class1 = [], []
    for object in train:
        if object[-1] == 1:
            class0.append(object)
        else:
            class1.append(object)
    class0 = np.array(class0)
    class1 = np.array(class1)

    xmin = min(min(class0[:, 0]), min(class1[:, 0])) - .5
    xmax = max(max(class0[:, 0]), max(class1[:, 0])) + .5
    ymin = min(min(class0[:, 1]), min(class1[:, 1])) - .5
    ymax = max(max(class0[:, 1]), max(class1[:, 1])) + .5

    xx, yy = np.meshgrid(np.arange(xmin, xmax, .1), np.arange(ymin, ymax, .1))
    Z = classifier.multi_predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.35)

    plt.scatter(train[:, 0], train[:, 1], c=train[:, 2])
    plt.title('Linear SVM Classifier')
    plt.show()

    print('Error = ', calculate_error(classifier, train))
