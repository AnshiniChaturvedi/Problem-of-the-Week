# Problem: Count Unival Subtrees (Google)

## Description
In many systems, especially in distributed trees or replicated data structures, it's important to 
find substructures that are uniform.  
A unival tree (short for universal value tree) is a subtree where all the nodes have the same value.  

You are given the root of a binary tree, and your task is to count the number of unival 
subtrees present in the tree.  

A single node is trivially considered a unival subtree.  

## Input Format
- You will be given the root of a binary tree. Each node contains:
  - An integer value
  - Left and right children

## Output Format
- Print a single integer: the number of unival subtrees.

## Constraints
- Number of nodes ≤ 1000
- Node values can be any integer (positive or negative)

## Example
  0
 / \
1   0
   / \
  1   0
 / \
1   1

##Output:
5

##Explanation:
The unival subtrees are:
1. The left leaf (1)  
2. The rightmost leaf (0)  
3. The two `1` leaves under the right subtree  
4. The subtree rooted at `1` (with both children also `1`)  
Total = 5



