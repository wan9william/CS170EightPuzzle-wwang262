class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent


class Tree:
    def __init__(self):
        self._root = None
        self._nodes = []

    def insert(self, parent, value):
        new_node = Node(value)
        if self._root is None:
            self._root = new_node
            self._nodes.append(new_node)
            return
        else:
            for node in self._nodes:
                if node.get_parent() == parent:
                    new_node.set_parent(node)
        return new_node

    def print_tree(self):
        if self._root is not None:
            level = 0
            stack = [self._root]
            while len(stack):
                node = stack.pop(0)
                for child in self._nodes:
                    if child.get_parent() == node:
                        stack.append(child)
                level += 1
        else:
            print("No tree")


t = Tree()
node1 = Node(2)
t.insert(node1, 3)
node2 = t.insert(node1,4)
node3 = t.insert(node2,4)
t.print_tree()
