from collections import deque 
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper Funtion to handle automatic BST insertion
def insert(root,data):
    if root is None:
        return TreeNode(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

# Create the BST 
# The root node is created first 
root = TreeNode(40)
# Inserting values automatically handles the left/right logic
# This builds a balanced-looking structure around 40
insert(root,10)
insert(root,20)
insert(root,30)
insert(root,50)
insert(root,60)
insert(root,70)
# Visually, the tree will now correctly look like this:
#        40
#      /    \
#    20      60
#   /  \    /  \
#  10  30  50  70

# ---- Verifying with Inorder Traversal ----
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("BST Inorder (Should be sorted):")
inorder(root) # Output will be: 10 20 30 40 50 60 70
print()