class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def invert_tree(root):
    if not root:
        return None
    root.left = invert_tree(root.right)
    root.right = invert_tree(root.left)
    return(root)


##test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
invert_tree(root)
