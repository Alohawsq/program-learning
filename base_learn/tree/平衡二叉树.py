"""
平衡二叉树
"""
from TreeNode import TreeNode

def is_balanced(root):
    def dfs(node):
        if not node:
            return True, 0
        # 递归检查左子树
        left_balanced, left_height = dfs(node.left)
        if not left_balanced:
            return False, 0
        # 递归检查右子树
        right_balanced, right_height = dfs(node.right)
        if not right_balanced:
            return False, 0  # 右子树不平衡，提前返回
        # 检查当前节点是否平衡
        if abs(left_height - right_height) > 1:
            return False, 0  # 当前节点不平衡
        # 当前节点平衡，返回高度（最大子树高度+1）
        return True, max(left_height, right_height) + 1

    is_balanced, tree_height = dfs(root)
    print(f"树是否平衡：{is_balanced}, 树高度：{tree_height}")
    return is_balanced


if __name__=='__main__':
    root = [3, 9, 20, None, None, 15, 7]
    root = TreeNode.create_tree(root)
    print(is_balanced(root))