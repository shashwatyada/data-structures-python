from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #     10
    #    /  \
    #   20   30
    #  / \   / \
    # 40 50 60 70

# Create Tree
root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left =  TreeNode(40)
root.left.right = TreeNode(50)

root.right.left = TreeNode(60)
root.right.right = TreeNode(70)

# Preorder Traversal 
def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# Inorder Traversal
def inorder(root):
    if root is None:
        return
    inorder(root.left) 
    print(root.data, end =" ")
    inorder(root.right)

# Postorder Traversal
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end =" ")

# Lavel Order Traversal
def level_order(root):
    if root is None:
        return 
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.data, end = " ")
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

# Height of the tree
def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)

    return max(left, right) +1    

# Count Total Nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Search Element 
def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    return search(root.left, key) or search(root.right, key)

# Maximum Value 
def find_max(root):
    if root is None:
        return 0
    return max(root.data,
               find_max(root.left),
               find_max(root.right))



print("Root : ", root.data)            # Parent
print("Left Child : ", root.left.data)       # Child
print("Right Child : ", root.right.data)
print("Left Left : ", root.left.left.data)  # Grandchild
print("Left Right : ", root.left.right.data)
print("Right Left : ", root.right.left.data)
print("Right Right : ", root.right.right.data)

print("\n")
print("Preorder Traversal : ")
preorder(root)
print("\n")

print("Inorder Traversal : ")
inorder(root)
print("\n")

print("Postorder Traversal : ")
postorder(root)
print("\n")

print("\nLevel Order Traversal")
level_order(root)
print("\n")

print("Height : ", height(root))
print("\n")

print("Total Nodes : ", count_nodes(root))
print("\n")

print("Search 50 : ", search(root,50))
print("\n")

print("Maximum :", find_max(root))