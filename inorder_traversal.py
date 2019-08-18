##binary tree inorder traversal
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

##inefficient way (recursive)
def inorderTraversal(root):
        res = []
        if root:
            res = inorderTraversal(root.left) 
            res.append(root.val)
            res = res + inorderTraversal(root.right)
        return res

##efficient way iteratively
def IterativeInorderTraversal(root):
    res,stack = [], [(root,False)]
    while stack:
        cur,visited = stack.pop()
        if cur:
            if visited:
                res.append(cur.val)
            else:
                stack.append((cur.right,False))
                stack.append((cur,True))
                stack.append((cur.left, False))
    return res




##test       
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
inorderTraversal(root)
IterativeInorderTraversal(root)