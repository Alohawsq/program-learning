class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def create_tree(arr):
        if not arr:
            return None
        queue = []
        root = TreeNode(arr[0])
        queue.append(root)
        i = 1
        while queue and i < len(arr):
            node = queue.pop(0)
            node.left = TreeNode(arr[i]) if arr[i] else None
            queue.append(node.left) if node.left else None
            node.right = TreeNode(arr[i + 1]) if (i+1) < len(arr) and arr[i + 1] else None
            queue.append(node.right) if node.right else None
            i += 2
        return root
