# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
  def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
      # Base case: If the node is None, return False
      if not root:
          return False

      # Subtract the value of the current node from the target sum
      targetSum -= root.val

      # If it's a leaf node, check if the remaining target sum is 0
      if not root.left and not root.right:
          return targetSum == 0

      # Recursively check the left and right subtrees
      return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Example usage:
        
