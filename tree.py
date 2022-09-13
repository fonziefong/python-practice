# tree.py

class TreeNode:
    def __init__(self, data):
        print("TreeNode __init__")
        self._data = data
        self._children = []

    @property
    def children(self):
        print("TreeNode children getter")
        return self._children

    @children.setter
    def children(self, value):
        print("TreeNode children setter")
        if isinstance(value, list):
            print(list)
            self._children = value
        else:
            del self.children
            print("deleted self.children: " + str(self.children))
            self._children.append(value)

    @children.deleter
    def children(self):
        print("TreeNode children deleter")
        self._children.clear()

    def __repr__(self):
        print("TreeNode def __repr__ " + self._data + " " + str(self.__class__.__name__))
        return f'{self.__class__.__name__}("{self._data}")'