from typing import List
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balancedBT(root:List[int])-> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0 
            
            left = height(root.left)
            #since yo chai dfs ma jancha let's add a optimization here
            if balanced[0] == False:
                return 0
            right = height(root.right)

            if abs(left-right)>1:
                balanced[0] = False
                return 0 

            return 1 + max(left,right)
    
        height(root)
        return balanced[0]
    
  