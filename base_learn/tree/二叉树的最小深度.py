"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
"""
from TreeNode import TreeNode

def min_depth(root):
    def dfs(root):
        if not root:
            return 0
        # 遍历左子树返回左子树高度
        left_height = dfs(root.left)
        # 遍历右子树返回右子树高度
        right_height = dfs(root.right)
        return min(left_height, right_height) + 1 if left_height and right_height else left_height + right_height + 1
    return dfs(root)

if __name__=='__main__':
    root = [3, 9, 20, None, None, 15, 7]
    root = [2, None, 3, None, 4, None, 5, None, 6]
    root = TreeNode.create_tree(root)
    print(min_depth(root))