# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def helper(self, root):
    #     if root == None:
    #         return
    #     temp = root.left
    #     root.left = root.right
    #     root.right = temp
    #     self.helper(root.left)
    #     self.helper(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.helper(root)
        # return root
        queue = [root]
        while len(queue) != 0:
            root = queue.pop(0)
            temp = root.left
            root.left = root.right
            root.right = temp
            queue.append(root.left)
            queue.append(root.right)
        return root