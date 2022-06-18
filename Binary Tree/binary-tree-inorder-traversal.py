# link to problem : https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack  = []
        ans = []
        while True:
                if curr is not None:
                    stack.append(curr)
                    curr = curr.left
                elif(stack):
                    curr = stack.pop()
                    print(curr.val)
                    ans.append(curr.val)
                    curr = curr.right
                else:
                    break
        return ans
                    
        
