import math

class Node(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.value = name
        self.children = children or []

    def __repr__(self):
        return f"Node({self.value}, {self.children})"

#    +
#   / \
#  1  *
#    / \
#   2   3
t = Node('+', [Node('1'),
               Node('*', [Node('2'),
                          Node('3')])])


""" 
t is a tree Node(+, [Node(1, []), Node(*, [Node(2, []), Node(3, [])])])
t.children returns a list of t's children e.g. [Node(1, []), Node(*, [Node(2, []), Node(3, [])])]
if a node u has no children then u.children would return an empty list [] - this is falsy, i.e. evaluates as boolean false.
"""

def countNodes(tree):
    if not tree.children: 
        return 1 # if a node has no children then there is only 1 node. 
    else:
        # for each child of the tree we need to calculate the number of children
        sum_of_children = sum([countNodes(child) for child in tree.children])
        return 1 + sum_of_children # add 1 to count the parent node. 

def computeTree(tree):
    if not tree.children: 
        return float(tree.value)
    else:
        # if a node has children then it must be an operator represented as a string e.g. '+' '*' '-'
        if tree.value == '+':
            return sum([computeTree(child) for child in tree.children])
        elif tree.value == '*':
            return math.prod([computeTree(child) for child in tree.children])
        else:
            raise NotImplementedError(f"Unsupported operator: {tree.value}")

print(computeTree(t))