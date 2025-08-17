# Count Unival Subtrees (Google)

## Problem
A unival subtree is one where all nodes have the same value.  
Given a binary tree root, count the number of unival subtrees.

## Example
  0
 / \
1   0
   / \
  1   0
 / \
1   1
Output: 5

## Approaches
### Approach 1: Recursive DFS
- Post-order traversal
- Check if left & right are unival and equal to root
- Time: O(N), Space: O(H)

### Approach 2: DFS with Tuple Return
- Each call returns (count, is_unival)
- Avoids global variable
- Time: O(N), Space: O(H)
