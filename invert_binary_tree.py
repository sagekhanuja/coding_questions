##objective: invert binary tree; images here: https://www.google.com/search?q=invert+binary+tree&sxsrf=ACYBGNSq2M7yWICoSt_41XW2b42j1C-vgQ:1566088912591&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiW-8jql4vkAhUiHTQIHcztAIwQ_AUIESgB&biw=1680&bih=876#imgrc=IELvKWSWRc_vMM:
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
