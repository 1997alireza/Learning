import pandas as pd
from tools import entropy, norm2_error
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Node:
    satisfying_gain = None

    def __init__(self, *classes_data, depth=0, satisfying_gain=None):
        self.classes_data = classes_data
        self.feature_splitter_index = -1  # if still it's -1 after the training so this is a terminal node
        self.feature_splitter_values = None
        self.children = None  # stand for the best class in terminal nodes
        self.depth = depth
        self.most_populous = -1  # best class in this node
        if satisfying_gain is not None:
            Node.satisfying_gain = satisfying_gain

    def entropy(self):
        return entropy(*[len(c_data) for c_data in self.classes_data])

    def get_total_data_size(self):
        return sum(len(c_data) for c_data in self.classes_data)

    def __find_most_populous(self):
        best_size = 0
        best_class = -1
        for c_iter, c_data in enumerate(self.classes_data):
            if len(c_data) > best_size:
                best_size = len(c_data)
                best_class = c_iter
        return best_class

    def make_best_splitter(self):
        # if self.depth > MAX_DEPTH:
        #     self.most_populous = self.__find_most_populous()
        #     self.children = self.most_populous
        #     return  # it's a terminal node

        not_zero_classes = 0
        for c_iter, c_data in enumerate(self.classes_data):
            if len(c_data) is not 0:
                if not_zero_classes == 0:
                    not_zero_classes = 1
                    self.children = c_iter
                else:
                    not_zero_classes = 2
                    break
        if not_zero_classes < 2:
            # print('--', self.depth)
            return  # it's a terminal node

        node_data_size = self.get_total_data_size()
        min_info_split = float('inf')

        for fi in range(num_of_features):
            fi_values = set([])
            for c_iter, c_data in enumerate(self.classes_data):
                c_data_f_values = []
                for d in c_data:
                    c_data_f_values.append(d[fi])
                fi_values = fi_values.union(set(c_data_f_values))
            fi_values = list(fi_values)

            children = []
            for i in range(len(fi_values)):
                init_data = []
                for j in range(len(self.classes_data)):
                    init_data.append([])
                children.append(Node(*init_data, depth=self.depth+1))

            for c_iter, c_data in enumerate(self.classes_data):
                for d in c_data:
                    d_fi = d[fi]
                    children[fi_values.index(d_fi)].classes_data[c_iter].append(d)

            info_split = 0
            for child in children:
                info_split += (child.get_total_data_size() / node_data_size) * child.entropy()

            if info_split < min_info_split:
                min_info_split = info_split
                self.feature_splitter_index = fi
                self.feature_splitter_values = fi_values
                self.children = children

        best_info_gain = self.entropy() - min_info_split  # best information gain

        self.most_populous = self.__find_most_populous()
        self.classes_data = None  # we don't need data in this node anymore

        if Node.satisfying_gain is not None and best_info_gain < Node.satisfying_gain:
            # print('depth & gain: ', self.depth, best_info_gain)
            self.feature_splitter_index = -1
            self.children = self.most_populous
            return  # it's a terminal node

        for c_id in range(len(self.children)):
            self.children[c_id].make_best_splitter()

    def get_class(self, x):
        if self.feature_splitter_index == -1:
            return self.children
        x_f_value = x[self.feature_splitter_index]
        if x_f_value in self.feature_splitter_values:
            child_index = self.feature_splitter_values.index(x_f_value)
            return self.children[child_index].get_class(x)
        return self.most_populous  # for other options that hadn't seen in the train data

    def get_number_of_nodes(self):
        if self.feature_splitter_index == -1:
            return 1
        return sum([child.get_number_of_nodes() for child in self.children]) + 1


# MAX_DEPTH = 700


if __name__ == '__main__':
    dataset = pd.read_csv('noisy_valid.csv')
    v_x = dataset.iloc[:, 1:].values.tolist()
    v_y = dataset.iloc[:, 0].values.tolist()
    dataset = pd.read_csv('noisy_train.csv')
    tr_x = dataset.iloc[:, 1:].values.tolist()
    tr_y = dataset.iloc[:, 0].values.tolist()
    dataset = pd.read_csv('noisy_test.csv')
    te_x = dataset.iloc[:, 1:].values.tolist()
    te_y = dataset.iloc[:, 0].values.tolist()

    num_of_features = len(v_x[0])

    class0_data = []
    class1_data = []
    for i in range(len(v_y)):
        if v_y[i] == 0:
            class0_data.append(v_x[i])
        else:
            class1_data.append(v_x[i])

    number_of_nodes = []
    valid_errs = []
    train_errs = []
    test_errs = []
    for i in range(1000):
        satisfying_gain = i / 1000
        print('satisfying gain:', satisfying_gain)
        decision_tree_r = Node(class0_data, class1_data, satisfying_gain=satisfying_gain)
        decision_tree_r.make_best_splitter()

        # print('Number of nodes:', decision_tree_r.get_number_of_nodes())
        number_of_nodes.append(decision_tree_r.get_number_of_nodes())

        y_pred_on_valid = []
        for i in range(len(v_x)):
            y_pred_on_valid.append(decision_tree_r.get_class(v_x[i]))
        # print('Error on valid data (euclidean distance): ', norm2_error(v_y, y_pred_on_valid))
        valid_errs.append(norm2_error(v_y, y_pred_on_valid))

        y_pred_on_train = []
        for i in range(len(tr_x)):
            y_pred_on_train.append(decision_tree_r.get_class(tr_x[i]))
        # print('Error on train data (euclidean distance): ', norm2_error(tr_y, y_pred_on_train))
        train_errs.append(norm2_error(tr_y, y_pred_on_train))

        y_pred_on_test = []
        for i in range(len(te_x)):
            y_pred_on_test.append(decision_tree_r.get_class(te_x[i]))
        # print('Error on test  data (euclidean distance): ', norm2_error(te_y, y_pred_on_test))
        test_errs.append(norm2_error(te_y, y_pred_on_test))

    plt.plot(number_of_nodes, valid_errs, 'b')
    plt.plot(number_of_nodes, train_errs, 'g')
    plt.plot(number_of_nodes, test_errs, 'r')

    plt.legend(handles=[
        mpatches.Patch(color='blue', label='valid'),
        mpatches.Patch(color='green', label='train'),
        mpatches.Patch(color='red', label='test')
    ])
    plt.xlabel('Number of nodes')
    plt.ylabel('Error (euclidean distance)')
    plt.show()
