# Problem: Word Search in 2D Matrix (Microsoft)

You are given a 2D matrix of characters and a target word. Your task is to check if the word exists in the matrix either:
- Left-to-right (horizontally), or
- Top-to-bottom (vertically).


## Input Format
- A 2D character matrix of size M × N
- A string representing the target word

## Output Format
- Return `true` if the word exists in the matrix (either row-wise or column-wise)
- Else return `false`.


## Constraints
- 1 ≤ M, N ≤ 100
- Word length ≤ max(M, N)
- All characters are uppercase English letters



## Example
Input:
matrix = [
['F', 'A', 'C', 'I'],
['O', 'B', 'Q', 'P'],
['A', 'N', 'O', 'B'],
['M', 'A', 'S', 'S']
]
word = "FOAM"

Output:
true

Explanation:
- "FOAM" appears in the first column (top-to-bottom).  
- "MASS" appears in the last row (left-to-right).