class APriori:

    def __init__(self, transactions, support_threshold=4):
        self.transactions = [set(i) for i in transactions]
        self._extract_labels_set()
        self.support_threshold = support_threshold

    def get_frequent_itemsets(self):
        frequent_itemsets = []  # index means the size of the subsets
        freq_iset_k = []
        for l in self._labels_set:
            base_itemset = set(l[0])
            sup = self._get_support(base_itemset)
            if sup >= self.support_threshold:
                freq_iset_k.append(ItemSet(base_itemset, sup))
        while len(freq_iset_k) > 0:
            frequent_itemsets.append(freq_iset_k)
            freq_iset_k = self._generate_next_itemsets(freq_iset_k)
        return frequent_itemsets

    @staticmethod
    def print_itemsets(itemsets):
        for ik in itemsets:
            print([i.items for i in ik])

    def _extract_labels_set(self):
        labels_set = set()
        for mis in self.transactions:
            for l in mis:
                labels_set.add(l)
        labels_set = list(labels_set)
        self._labels_set = labels_set

    def _generate_next_itemsets(self, fi_k):
        k = len(fi_k[0].items)
        fi_next = []
        for l in self._labels_set:
            for fi_k_i in fi_k:
                copy = set(fi_k_i.items)
                copy.add(l)
                if len(copy) == k+1:
                    sup = self._get_support(copy)
                    if sup >= self.support_threshold:
                        fi_next.append(ItemSet(copy, sup))
        return fi_next

    def _get_support(self, itemset):
        seen_count = 0
        for t in self.transactions:
            ok = True
            for l in itemset:
                if l not in t:
                    ok = False
                    break
            if ok:
                seen_count += 1
        return seen_count

class ItemSet:
    items: {} = None
    support: int = 0

    def __init__(self, items, support):
        self.items = items
        self.support = support


class AssociationRule:
    left_items: {} = None
    right_items: {} = None
    support: int = 0
    confidence: int = 0

    def __init__(self, left_items, right_items, support, confidence):
        self.left_items = left_items
        self.right_items = right_items
        self.support = support
        self.confidence = confidence


if __name__ == '__main__':
    transactions = [
        ['a', 'b', 'd', 'g'],
        ['b', 'd', 'e'],
        ['a', 'b', 'c', 'e', 'f'],
        ['b', 'd', 'e', 'g'],
        ['a', 'b', 'c', 'e', 'f'],
        ['b', 'e', 'g'],
        ['a', 'c', 'd', 'e'],
        ['b', 'e'],
        ['a', 'b', 'e', 'f'],
        ['a', 'c', 'd', 'e']
    ]

    a_priori_solver = APriori(transactions)
    APriori.print_itemsets(a_priori_solver.get_frequent_itemsets())
