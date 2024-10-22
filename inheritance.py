# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, item):
#         self.stack.append(item)
#     def pop(self):
#         return self.stack.pop()
#     def peek(self):
#         return self.stack(len(self.stack)-1)
#     def __str__(self):
#         return str(self.stack)
    
# stack1 = Stack()
# stack1.push(1)
# stack1.push(2)
# stack1.push(3)
# print(stack1)
# print(stack1.pop())

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self,root):
        self.root = Node(root)

    def preorder(self, start, records):
        if start:
            records.append(start.value)
            records = self.preorder(start.left, records)
            records = self.preorder(start.right, records)
        return records
    
    def postorder(self, start, records):
        if start:
            records = self.postorder(start.left, records)
            records = self.postorder(start.right, records)
            records.append(start.value)
        return records
tree = Tree(5)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(2)
tree.root.left.right = Node(8)
print(tree.preorder(tree.root, []))