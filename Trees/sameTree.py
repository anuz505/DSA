# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p or not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        return (self.isSameTree(p.left,q.left)and self.isSameTree(p.right,q.right))
    
if __name__ == "__main__":
    # Example usage:
    # Construct two trees:
    #     1         1
    #    / \       / \
    #   2   3     2   3

    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    sol = Solution()
    print(sol.isSameTree(tree1, tree2))  # Output: True

    # Modify tree2 to be different
    tree2.right.val = 4
    print(sol.isSameTree(tree1, tree2))  # Output: False