# Problem: Equal Sum Partition (Facebook)

## Description
You are given a multiset (a list that can have duplicate integers).  
Determine whether it can be partitioned into two subsets such that the sum of elements in both subsets is equal.  

This is a variation of the Subset Sum Problem and is known as the **Partition Equal Subset Sum** problem.

## Input Format
- A list of integers (can include duplicates).  
- The list may contain up to 100 elements.  

## Output Format
- Return `true` if the set can be partitioned into two subsets with equal sum, else return `false`.

## Constraints
- All numbers are non-negative integers.  
- At least one number exists in the input.

## Example 1
Input:
[15, 5, 20, 10, 35, 15, 10]
Output:
true


Explanation:
Subset1 = [15, 5, 10, 15, 10] → Sum = 55  
Subset2 = [20, 35] → Sum = 55  

## Example 2
Input: 
[15, 5, 20, 10, 35]

Output:
false

Explanation:
Total sum = 85 (odd) → cannot be split equally.

