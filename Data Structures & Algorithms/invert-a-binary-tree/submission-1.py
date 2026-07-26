# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #recursive function that switches child legs and goes down the tree
        def helper(node: Optional[TreeNode]) ->None: 
            if not node: 
                return None
            
            tmp = node.left
            node.left = node.right
            node.right = tmp

            helper(node.left)
            helper(node.right)

        if not root:
            return None
            
        helper(root)
        return root
            