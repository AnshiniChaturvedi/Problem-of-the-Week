# Flood Fill Algorithm (Facebook)

## Problem Statement
Given an image (2D matrix), starting pixel `(sr, sc)`, and a new color `C`, perform a flood fill.

Change the starting pixel and all 4-directionally connected pixels of the same original color to `C`.

### Example
Input:
image = [
['B', 'B', 'W'],
['W', 'W', 'W'],
['W', 'W', 'W'],
['B', 'B', 'B']
]
sr = 2, sc = 2, C = 'G'

Output:
[
['B', 'B', 'G'],
['G', 'G', 'G'],
['G', 'G', 'G'],
['B', 'B', 'B']
]