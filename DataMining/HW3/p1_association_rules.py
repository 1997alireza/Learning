from dataclasses import dataclass


@dataclass
class ItemSet:
    items: {} = None
    support: int = 0

    def __init__(self, items, support):
        self.items = items
        self.support = support


@dataclass
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


class APriori:

    frequent_itemsets = None

    def __init__(self, transactions, support_threshold=4):
        self.transactions = [set(i) for i in transactions]
        self._extract_labels_set()
        self.support_threshold = support_threshold

    def extract_frequent_itemsets(self):  # a_priori
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
        self.frequent_itemsets = frequent_itemsets

    def extract_association_rules(self, min_confidence=.5):
        if self.frequent_itemsets is None:
            self.extract_frequent_itemsets()
        rules = []
        for k in range(len(self.frequent_itemsets)):
            for itemset in self.frequent_itemsets[k]:
                rules.extend(self._generate_association_rules(itemset, min_confidence))
        return rules

    def _generate_association_rules(self, itemset: ItemSet, min_confidence):
        items = list(itemset.items)
        num = len(items)
        rules = []
        for c in range(1, pow(2, num)-1):
            existence = format(c, 'b')[::-1]
            left, right = set(), set()
            for i in range(num):
                if i >= len(existence) or existence[i] == '0':
                    left.add(items[i])
                else:
                    right.add(items[i])
            conf = itemset.support / self._get_support(left)
            if conf >= min_confidence:
                rules.append(AssociationRule(left, right, itemset.support, conf))

        return rules

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
                    new_itemset = ItemSet(copy, sup)
                    if sup >= self.support_threshold and new_itemset not in fi_next:
                        fi_next.append(new_itemset)
        return fi_next

    def _get_support(self, itemset: set):
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
