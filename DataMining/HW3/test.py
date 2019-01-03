from p1a import *
from tools import *

if __name__ == '__main__':

    # =========== Question One - Part One ==========
    # transactions = [
    #     ['a', 'b', 'd', 'g'],
    #     ['b', 'd', 'e'],
    #     ['a', 'b', 'c', 'e', 'f'],
    #     ['b', 'd', 'e', 'g'],
    #     ['a', 'b', 'c', 'e', 'f'],
    #     ['b', 'e', 'g'],
    #     ['a', 'c', 'd', 'e'],
    #     ['b', 'e'],
    #     ['a', 'b', 'e', 'f'],
    #     ['a', 'c', 'd', 'e']
    # ]
    #
    # a_priori_solver = APriori(transactions)
    # a_priori_solver.extract_frequent_itemsets()

    # print([x.items for x in a_priori_solver.frequent_itemsets[0]])  # frequent 1-itemsets, 1.a
    # print([x.items for x in a_priori_solver.frequent_itemsets[1]])  # frequent 2-itemsets, 1.b

    # two_itemsets = a_priori_solver.frequent_itemsets[1] # 1.c
    # for itemset in two_itemsets:
    #     if itemset.support >= 7:
    #         print(itemset)

    # print(*a_priori_solver.extract_association_rules(1.0), sep='\n')  # 1.d
    # print(*a_priori_solver.extract_association_rules(0), sep='\n')  # 1.e


    # =========== Question One - Part Two ==========

    transactions = [
        ['a', 'c', 'd'],
        ['b', 'c', 'e'],
        ['a', 'b', 'c', 'e'],
        ['b', 'e']
    ]

    a_priori_solver = APriori(transactions, support_threshold=2)
    a_priori_solver.extract_frequent_itemsets()
    # print_itemsets(a_priori_solver.frequent_itemsets)  # 1.a
    # print(len(a_priori_solver.extract_association_rules(.65)))  # 1.b
    # print(*a_priori_solver.extract_association_rules(0.8), sep='\n')  # 1.c
    # print(*a_priori_solver.extract_association_rules(0), sep='\n')  # 1.d, 1.e

