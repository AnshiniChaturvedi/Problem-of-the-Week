# Word Search in 2D Matrix (Microsoft)

## Problem
Check if word exists in matrix left-to-right or top-to-bottom.

## Example
Matrix:
[
 ['F','A','C','I'],
 ['O','B','Q','P'],
 ['A','N','O','B'],
 ['M','A','S','S']
]
Word: "FOAM" → True

## Approaches
### Approach 1: Row & Column Scan
- Build strings row-wise & column-wise
- Check substring
- Time: O(M*N), Space: O(1)

### Approach 2: Transpose Matrix
- Convert rows and columns into strings
- Search in combined list
- Time: O(M*N), Space: O(M+N)
