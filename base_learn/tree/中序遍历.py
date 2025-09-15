from typing import Optional, List
from TreeNode import TreeNode
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node):
            if node:
                # 访问左子树
                dfs(node.left)
                # 访问根节点
                result.append(node.val)
                # 访问右子树
                dfs(node.right)
        dfs(root)
        return result


if __name__ == "__main__":
    root = [1, None, 2, 3]
    root = TreeNode.create_tree(root)
    print(Solution().inorderTraversal(root))