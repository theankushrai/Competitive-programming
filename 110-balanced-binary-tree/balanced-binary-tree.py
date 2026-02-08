# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def is_balanced(node,height) :
            if not node:
                return True,height
            
            left, left_height = is_balanced(node.left,height+1)
            right,right_height=is_balanced(node.right,height+1)

            if left and right and abs(left_height-right_height)<=1:
                return True,max(left_height,right_height)
            return False,max(left_height,right_height)
        
        return is_balanced(root,0)[0]
                  

        