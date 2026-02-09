# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        inorder_array=[]
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nonlocal inorder_array
            inorder_array.append(node.val)
            inorder(node.right)
        
        inorder(root)

        def create_balanced_tree(start,end,arr):
            if start>end:
                return None
            mid=(start+end)//2
            node = TreeNode(arr[mid])
            node.left=create_balanced_tree(start,mid-1,arr)
            node.right=create_balanced_tree(mid+1,end,arr)
            return node
        
        return create_balanced_tree(0,len(inorder_array)-1,inorder_array)

