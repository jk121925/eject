from typing import Set
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left: None | Node = None
        self.right: None | Node = None



rootNode = Node(0)
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
rootNode.left = Node1
rootNode.right = Node2

Node1.left = Node3
Node1.right = Node4
Node2.left = Node5
Node2.right = Node6

"""
    0
  /   \
  1    2
/  \  / \
3  4  5  6

"""

#Pre order
def preorder_loop(root_node:Node)-> None:
    stack = []
    stack.append(root_node)
    while len(stack) > 0:
        cur = stack.pop()
        print(cur.value)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


print("preorder_loop")
preorder_loop(rootNode)
print("")

#in order
def inorder_loop(root_node:Node) -> None:
    stack = []
    visited: Set[Node] = set()
    stack.append(root_node.right)
    stack.append(root_node)
    visited.add(root_node)
    stack.append(root_node.left)
    while len(stack) > 0:
        cur = stack.pop()
        assert cur is not None
        if cur in visited:
            print(cur.value)
        else:
            visited.add(cur)
            if cur.right:
                stack.append(cur.right)
            stack.append(cur)
            if cur.left:
                stack.append(cur.left)
print("inorder_loop")
inorder_loop(rootNode)
print()


def postorder(root_node:Node) -> None:
    stack = []
    visited: Set[Node] = set()
    assert root_node is not None
    visited.add(root_node)
    stack.append(root_node)
    if root_node.right:
        stack.append(root_node.right)
    if root_node.left:
        stack.append(root_node.left)
    while len(stack) > 0:
        cur = stack.pop()
        if cur in visited:
            print(cur.value)
        else:
            visited.add(cur)
            stack.append(cur)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

print("postorder")
postorder(rootNode)
print()
