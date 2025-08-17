# Equal Sum Partition (Facebook)

## Problem
Check if array can be split into 2 subsets with equal sum.

## Example
Input: [15, 5, 20, 10, 35, 15, 10]  
Output: True

## Approaches
### Approach 1: Recursive + Memoization
- Try including/excluding elements
- Memoize overlapping subproblems
- Time: O(N * target), Space: O(N * target)

### Approach 2: Dynamic Programming
- Bottom-up DP
- dp[j] means "can we reach sum j?"
- Time: O(N * target), Space: O(target)
