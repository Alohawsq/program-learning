"""
给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
"""
from TreeNode import TreeNode

def max_depth(root):
    def dfs(root):
        if not root:
            return 0
        # 遍历左子树返回左子树高度
        left_height = dfs(root.left)
        # 遍历右子树返回右子树高度
        right_height = dfs(root.right)
        return max(left_height, right_height) + 1

    return dfs(root)

if __name__=='__main__':
    root = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.create_tree(root)
    print(max_depth(root))
