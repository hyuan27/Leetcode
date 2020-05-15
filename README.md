# Leetcode

## 1. Two Sum

Two ways: 

1. O(N^2): double loop (easy way)

2. O(N): Use hash map, the solution is a one pass solution

## 2. Add Two Numbers

Three Ways: 
1. O(m+n): Traverse each list, get number, add, and then put the sum into a new list, very naive solution

2. O(max(m,n)): Traverse at same time

3. O(min(m,n)): Traverse at same time, but add condition at the end of loop, if one is empty and one is not, simply copy over the entire leftover. 
