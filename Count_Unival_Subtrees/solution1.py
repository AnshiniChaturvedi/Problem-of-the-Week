class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root):
    count = [0]

    def is_unival(node):
        if not node:
            return True
        left = is_unival(node.left)
        right = is_unival(node.right)

        if not left or not right:
            return False
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False

        count[0] += 1
        return True

    is_unival(root)
    return count[0]

# Example
root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(count_unival_subtrees(root))  # Output: 5
