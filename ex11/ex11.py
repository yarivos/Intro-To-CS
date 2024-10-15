import copy
import itertools
from queue import Queue

from typing import List


class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

    def __str__(self):
        return str(self.data)

    def display(self):
        res = ""
        lines, *_ = self._display_aux()
        for line in lines:
            res += line + "\n"
        return res

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.negative_child is None and self.positive_child is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.negative_child is None:
            lines, n, p, x = self.positive_child._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.positive_child is None:
            lines, n, p, x = self.negative_child._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.positive_child._display_aux()
        right, m, q, y = self.negative_child._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
                     '' + s + y * '' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
                      (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Record:
    def __init__(self, illness: str, symptoms: list):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root: Node):
        self.root = root
        self.flag = False

    def diagnose(self, symptoms) -> str:
        """
        function will run through list of symptoms and find the leaf that matches
        the symptoms in list.
        :param symptoms:list of strings
        :return:a leaf which is the illness described by the symptoms
        """
        current_node = self.root
        while True:
            if current_node.positive_child is None and current_node.negative_child is None:
                return current_node.data
            if current_node.data in symptoms:
                current_node = current_node.positive_child
            else:
                current_node = current_node.negative_child

    def calculate_success_rate(self, records) -> float:
        """
        checks how many successive diagnoses were done by
        the function diagnose on records
        :param records: a list, contains [illness, list of symptoms]
        :return: percentage of accuracy of the root tree.
        """
        if len(records) == 0:
            raise ValueError("records list is empty!")
        correct_diagnose_count = 0
        for record in records:
            if self.diagnose(record.symptoms) == record.illness:
                correct_diagnose_count += 1
        return correct_diagnose_count / len(records)  # ratio of success

    def all_illnesses(self):
        """
        runs through the root tree with recursion to return a list of illnesses in
        the tree. the list is sorted from most occurring illness to least
        :return: A list of illnesses
        """
        dict_of_illnesses = {}
        self.all_illnesses_helper(self.root, dict_of_illnesses)
        sort_dict = sorted(dict_of_illnesses.items(), key=lambda x: x[1], reverse=True)
        list_of_illnesses = []
        for value in sort_dict:
            list_of_illnesses.append(value[0])
        return list_of_illnesses

    def all_illnesses_helper(self, node, dict_of_illnesses):
        if node.positive_child is None and node.negative_child is None:
            if node.data:
                if node.data in dict_of_illnesses:  # adds the illness to the dictionary
                    dict_of_illnesses[node.data] += 1
                else:
                    dict_of_illnesses[node.data] = 1
        if node.positive_child is not None:
            self.all_illnesses_helper(node.positive_child, dict_of_illnesses)
        if node.negative_child is not None:
            self.all_illnesses_helper(node.negative_child, dict_of_illnesses)

    def paths_to_illness(self, illness):
        """
        runs through the root tree to find the path to the "illness" argument

        :param illness:
        :return: paths to illness is a list with paths using True and False to
        indicate the direction in the tree
        """
        list_of_paths = []
        self.paths_to_illness_helper(self.root, illness, list_of_paths, [])
        return list_of_paths

    def paths_to_illness_helper(self, node, illness, list_of_paths, path):
        if node.positive_child is None and node.negative_child is None:
            if node.data == illness:
                list_of_paths.append(copy.copy(path))
        if node.positive_child is not None:
            path.append(True)
            self.paths_to_illness_helper(node.positive_child, illness, list_of_paths, path)
            path.pop()
        if node.negative_child is not None:
            path.append(False)
            self.paths_to_illness_helper(node.negative_child, illness, list_of_paths, path)
            path.pop()

    def minimize(self, remove_empty=False):
        """this function will 'cut' part of the the tree which are redundant"""
        self.flag = False
        self.tree_iterator(self.root)
        if remove_empty:
            self.tree_iterator2(self.root, None, "")




    def leaf_finder(self, node, leaves):
        """puts all of leaves data into the list"""
        if not node.positive_child and not node.negative_child:
            leaves.append(node.data)
        if node.positive_child:
            self.leaf_finder(node.positive_child, leaves)
        if node.negative_child:
            self.leaf_finder(node.negative_child, leaves)

    def tree_iterator2(self, root, father, side):
        """iterates over the whole tree"""
        if root.positive_child and root.negative_child:
            lst1 = []
            self.leaf_finder(root, lst1)
            if lst1 == [None] * len(lst1):
                self.flag = True
                if father is None:
                    self.root = Node(None, None, None)
                if side == "pos":
                    father.positive_child = father.negative_child
                else:
                    father.negative_child = father.positive_child
        if root.positive_child:
            self.tree_iterator2(root.positive_child, root, "pos")
        if root.negative_child:
            self.tree_iterator2(root.negative_child, root, "neg")

    def tree_iterator(self, root):
        """
        iterates over all of the tree
        :param root:
        :return:
        """
        if root.positive_child and root.negative_child:
            self.minimize_helper(root)
        if root.positive_child:
            self.tree_iterator(root.positive_child)
        if root.negative_child:
            self.tree_iterator(root.negative_child)

    def minimize_helper(self, root):
        pos_node = root.positive_child
        neg_node = root.negative_child
        if same_tree_check(pos_node, neg_node):
            self.flag = True
            root = pos_node  # change tree to one of its children


def same_tree_check(root1, root2):
    """
    checks if two roots are identical
    :param root1:
    :param root2:
    :return:
    """
    queue1 = Queue()
    queue2 = Queue()
    queue1.put(root1)
    queue2.put(root2)
    return same_tree_helper(queue1, queue2)


def same_tree_helper(queue1, queue2):
    while not queue1.empty() and not queue2.empty():  # iterates until reaching the leaf
        next_node1 = queue1.queue[0]
        next_node2 = queue2.queue[0]
        if next_node1.data != next_node2.data:  # if nodes are different -> trees are not identical
            return False
        queue1.get()
        queue2.get()
        if next_node1.negative_child and next_node2.negative_child:  # checks if negative child exists for both trees
            queue1.put(next_node1.negative_child)
            queue2.put(next_node2.negative_child)
        elif next_node1.negative_child or next_node2.negative_child:  # checks if negative child exists for both trees
            return False
        if next_node1.positive_child and next_node2.positive_child:  # checks if positive child exists for both trees
            queue1.put(next_node1.positive_child)
            queue2.put(next_node2.positive_child)
        elif next_node1.positive_child or next_node2.positive_child:  # checks if positive child exists for both trees
            return False
    return True


def build_tree(records, symptoms):
    """
    builds a tree using symptoms and records and return an object Diagnoser
    with the tree in it
    :param records:
    :param symptoms:
    :return:
    """
    if len(symptoms) == 0:
        lst_of_illness = []
        for record in records:
            lst_of_illness.append(record.illness)
        freq_ill = max(lst_of_illness, key=lst_of_illness.count)
        return Diagnoser(Node(freq_ill, None, None))
    build_tree_check(records, symptoms)
    node = Node(symptoms[0], None, None)
    build_initial_tree(node, symptoms[1:])
    put_illness(node, [], [], records)
    diagnose_ob = Diagnoser(node)
    return diagnose_ob


def build_initial_tree(node, symptoms):
    """
    builds a tree of symptoms, symptom[0] as the root and child data = symptoms[1]
    and so on.
    :param node:
    :param symptoms:
    :return:
    """
    if len(symptoms) == 0:
        node1 = Node(None, None, None)
        node2 = Node(None, None, None)
        node.positive_child = node1
        node.negative_child = node2
        return
    node1 = Node(symptoms[0], None, None)
    node2 = Node(symptoms[0], None, None)
    node.positive_child = node1
    node.negative_child = node2
    build_initial_tree(node1, symptoms[1:])
    build_initial_tree(node2, symptoms[1:])


def put_illness(node, pos_path, neg_path, records):
    """
    puts the correct illness in the spot of the leaf according to path of symptoms
    :param node:
    :param path: a list of syptoms
    :param records:
    :return:
    """
    if not node.data:
        node.data = find_right_illness(pos_path, neg_path, records)
        return
    pos_path.append(node.data)
    put_illness(node.positive_child, pos_path, neg_path, records)
    pos_path.pop()
    neg_path.append(node.data)
    put_illness(node.negative_child, pos_path, neg_path, records)
    neg_path.pop()


def find_right_illness(pos_path, neg_path, records):
    """
    receives a list of symptoms and returns the most likely illness according to records
    :param path:
    :param records:
    :return:
    """
    dict_of_illness = {}
    for record in records:  # iterates over all the records
        Flag_pos = True
        Flag_neg = True
        for symptom_in_path in pos_path:
            if symptom_in_path not in record.symptoms:
                Flag_pos = False
                break
        for symptom_in_path in neg_path:
            if symptom_in_path in record.symptoms:
                Flag_neg = False
                break
        if Flag_pos and Flag_neg:
            if record.illness in dict_of_illness:  # adds the illness to the dictionary
                dict_of_illness[record.illness] += 1
            else:
                dict_of_illness[record.illness] = 1
    if len(dict_of_illness) == 0:
        return None
    max_key = max(dict_of_illness, key=lambda k: dict_of_illness[k])
    return max_key


def build_tree_check(records, symptoms):
    """
    check if arguments are valid
    :param records:
    :param symptoms:
    :return:
    """
    for record in records:
        if type(record) != Record:
            raise TypeError("records argument needs to hold only type Record Objects")
        for symptom in record.symptoms:
            if type(symptom) != str:
                raise TypeError("symptoms list needs to hold only type String Objects")
    for symptom in symptoms:
        if type(symptom) != str:
            raise TypeError("symptoms list needs to hold only type String Objects")


def optimal_tree_check(records, symptoms, depth):
    if not 0 <= depth <= len(symptoms):  # if depth value is invalid
        raise ValueError("parameter - 'depth' value is invalid")
    for record in records:
        if type(record) != Record:
            raise TypeError("records argument needs to hold only type Record Objects")
        for symptom in record.symptoms:
            if type(symptom) != str:
                raise TypeError("symptoms list needs to hold only type String Objects")
            if record.symptoms.count(symptom) != 1:
                raise ValueError("list of symptoms can't contain a symptom more than once\n"
                                 "this symptom " + symptom + "occurred more than once")
    for symptom in symptoms:
        if type(symptom) != str:
            raise TypeError("symptoms list needs to hold only type String Objects")
        if symptoms.count(symptom) != 1:
            raise ValueError("list of symptoms can't contain a symptom more than once\n"
                             "this symptom " + symptom + "occurred more than once")


def optimal_tree(records, symptoms, depth):
    optimal_tree_check(records, symptoms, depth)
    if depth == 0:
        lst_of_illness = []
        for record in records:
            lst_of_illness.append(record.illness)
        freq_ill = max(lst_of_illness, key=lst_of_illness.count)
        return Diagnoser(Node(freq_ill, None, None))
    comb_of_symptoms = list(itertools.combinations(symptoms, depth))
    print(comb_of_symptoms)
    lst_diagnoses = []
    for symptoms_option in comb_of_symptoms:  # runs through all optional trees
        curr_diagnose = build_tree(records, symptoms_option)
        success_rate = curr_diagnose.calculate_success_rate(records)
        lst_diagnoses.append((curr_diagnose, success_rate))
    print(lst_diagnoses)
    optimal_diagnose = max(lst_diagnoses, key=lambda x: x[1])
    return optimal_diagnose[0]


def in_order_traversal(node):
    if node.positive_child:
        in_order_traversal(node.positive_child)
    if node.positive_child is None and node.negative_child is None:
        print(node)
    if node.negative_child:
        in_order_traversal(node.negative_child)


if __name__ == "__main__":
    record1 = Record("influenza", ["cough", "fever"])
# record2 = Record("cold", ["cough"])
# records = [record1, record2]
# x: Diagnoser = build_tree(records, ["fever"])
# y: Diagnoser = optimal_tree(records, ["cough", "fever"], 1)
# print(x.root.display())
# print(y.root.display())
# Manually build a simple tree.
#                cough
#          Yes /       \ No
#        fever           pipi
#   Yes /     \ No   Yes/   \No
# covid-19   cold   covid   healthy

# flu_leaf = Node("covid-19", None, None)
# cold_leaf = Node("cold", None, None)
# flu_leaf2 = Node("covid-19", None, None)
# cold_leaf2 = Node("healthy", None, None)
# inner_vertex = Node("fever", flu_leaf, cold_leaf)
# healthy_leaf = Node("pipi", flu_leaf2, cold_leaf2)
# root = Node("cough", inner_vertex, healthy_leaf)
# diagnoser = Diagnoser(root)

# # Simple test for "diagnose" function
# diagnosis = diagnoser.diagnose(["cough"])
# if diagnosis == "cold":
#     print("Test passed")
# else:
#     print("Test failed. Should have printed cold, printed: ", diagnosis)
# # Simple test for "all.illnesses" function
# illnesses = diagnoser.all_illnesses()
# if illnesses == ["covid-19", "cold", "healthy"]:
#     print("Test passed")
# else:
#     print("Test failed, printed: ", illnesses)
# # Simple test for "path_to_illness" function
# illness_path = diagnoser.paths_to_illness("covid-19")
# if illness_path == [[True, True], [False, True]]:
#     print("Test passed")
# else:
#     print("Test failed, printed", illness_path)
# Simple test for build_tree function
# lst1 = ["cough", "fatigue", "sore_throat", "headache", "fever", "nausea"]
# node = Node(lst1[0], None, None)
# lst2 = [
#     Record("strep###########",
#            ["cough", "fatigue", "sore_throat", "headache", "fever", "nausea"]),
#     Record("cold###########", ["cough", "headache"]),
#     Record("mono########", ["fatigue", "sore_throat", "headache"]), Record("healthy##########", []),
#     Record("meningitis##########", ["headache", "fever"]),
#     Record("influenza##########", ["cough", "fatigue", "headache", "nausea"])]
# x = build_tree(lst2, lst1)
# print(x.root.display())

# Add more tests for sections 2-7 here.
