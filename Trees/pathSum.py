class Solution:
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, sum):
            if not node:
                return False
            sum += node.val
            # leaf node check 
            if not node.left and not node.right:
                return sum == targetSum
            return dfs(node.left,sum) or dfs(node.right,sum)
        return dfs(root,0)
        
        



if __name__=="__main__":
    # Example usage:
    # Define a simple TreeNode class for testing
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Build a sample tree:
    #     5
    #    / \
    #   4   8
    #  /   / \
    # 11  13  4
    # /  \      \
    #7    2      1

    root = TreeNode(5)
    root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))

    sol = Solution()
    print(sol.hasPathSum(root, 22))  # Expected output: True