from tree import TreeNode

print("Code: root = TreeNode(\"root\")")
root = TreeNode("root")
print("Code: child1 = TreeNode(\"child 1\")")
child1 = TreeNode("child 1")
print("Code: child2 = TreeNode(\"child 2\")")
child2 = TreeNode("child 2")
print("Code: child3 = TreeNode(\"child 2\")")
child3 = TreeNode("child 3")

print("Code: root.children = [child1, child2]")
root.children = [child1, child2]

print("Code: root.children")
root.children
print("Code: print(root.children)")
print(root.children)

print("Code: print(child3.children)")
print(child3.children)
print("Code: root.children = child3")
root.children = child3

print("Code: root.children")
root.children
print("Code: print(root.children)")
print(root.children)


print("Code: del root.children")
del root.children
print("Code: root.children")
root.children