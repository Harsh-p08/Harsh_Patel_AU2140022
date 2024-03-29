# -*- coding: utf-8 -*-
"""Lab_7_Trees

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nLTq5bpzHDmLO8r7ZMxZhWoI_WYOc-AP

Name : Harsh DineshKumar Patel 


Roll No.: AU2140022



DSA Section 1
"""

# Problem 1 (1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_tree(root):
    stack = []
    if root is None:
        return
    stack.append(root)
    while len(stack) > 0:
        root = stack.pop()
        print(root.data, end = " ")
        if root.right != None:
            stack.append(root.right)
        if root.left != None:
            stack.append(root.left)

root = Node(5)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(4)
root.right.right = Node(9)
preorder_tree(root)

# Problem 1 (2)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_tree(root):
    stack = []
    while True:
        if root != None:
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop()
            print(root.data, end = " ")
            root = root.right
        else:
            break

root = Node(5)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(4)
root.right.right = Node(9)
inorder_tree(root)

# Problem 1 (3)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder_tree(root):
    stack = []
    while True:
        while root != None:
            stack.append(root)
            stack.append(root)
            root = root.left
        if len(stack) == 0:
            return
        root = stack.pop()
        if len(stack) > 0 and stack[-1] == root:
            root = root.right
        else:
            print(root.data, end = " ")
            root = None

root = Node(5)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(4)
root.right.right = Node(9)
postorder_tree(root)

# Problem 2

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, data):
        self.elements.append(data)
        return data

    def dequeue(self):
        return self.elements.pop(0)
    
    def rear(self):
        return self.elements[-1]
    
    def front(self):
        return self.elements[0]
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def size(self):
        return len(self.elements)

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
    
def bfs(root):
    if root is None:
        return []
    q = Queue()
    q.enqueue(root)
    ans = []
    while not q.is_empty():
        n = q.size()
        v = []
        for i in range(0, n):
            temp = q.front()
            q.dequeue()
            for i in temp.children:
                q.enqueue(i)
            v.append(temp.data)
        ans.append(v)
    return list(ans)

def take_input():
    print("Data:", end = ' ')
    data = input()
    if data == - 1:
        return None
    temp = Node(data)
    print("Enter the number of children of ", end = '')
    print(data, end = '')
    print(" : ", end = '')
    n = int(input())
    for i in range(0, n):
        print("Enter ", end = '')
        print(i+1, end = '')
        print("th child of ", end = '')
        print(data, end = '')
        print("\n", end = '')
        child = take_input()
        temp.children.append(child)
    return temp

# Problem 3

def min_heap(array, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[l] < array[smallest]:
        smallest = l
    if r < n and array[r] < array[smallest]:
        smallest = r
    if smallest != i:
        (array[i],
         array[smallest]) = (array[smallest], array[i])
        min_heap(array, n, smallest)

def heapSort(array):
    n = len(array)
    for i in range(int(n / 2) - 1, -1, -1):
        min_heap(array, n, i)
    for i in range(n-1, -1, -1):
        array[0], array[i] = array[i], array[0]
        min_heap(array, i, 0)
    return array

arr = [5,3,1,6,8,14,10]
print("Array Before MinHeap is: ", arr)
print("Heap Sort using MinHeap is: ", heapSort(arr))

# Problem 4

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    stack = []
    while True:
        if root != None:
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop()
            print(root.data, end = " ")
            root = root.right
        else:
            break

def insert(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

def min_node(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif(data > root.data):
        root.right = deleteNode(root.right, data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_node(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

def min_value(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current.data

r = None
r = insert(r, -5)
r = insert(r, 8)
r = insert(r, 6)
r = insert(r, 2)
r = insert(r, 7)
r = insert(r, 15)
r = insert(r, 9)
r = insert(r, 32)

print("Inorder traversal: ", end=' ')
inorder(r)
print("\nDeleting 15")
r = deleteNode(r, 15)
print("Inorder traversal: ", end=' ')
inorder(r)
print("\nMinimum value is: ", min_value(r))