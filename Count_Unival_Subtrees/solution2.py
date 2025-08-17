def count_unival_subtrees_optimized(root):
    def helper(node):
        if not node:
            return (0, True)
        left_count, left_uni = helper(node.left)
        right_count, right_uni = helper(node.right)

        total = left_count + right_count
        if left_uni and right_uni:
            if (not node.left or node.left.val == node.val) and \
               (not node.right or node.right.val == node.val):
                return (total + 1, True)
        return (total, False)

    return helper(root)[0]
