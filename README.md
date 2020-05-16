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

## 3. Longest Substring Without Repeating Characters

Two ways: 

1. O(n^3): brute force to find all substrings and check

2. O(n): only go through once, update the start index pointer

## 7. Reverse Integer:

Two ways

1. Use module and divide to find each digit and reverse, slow

2. Change to string, reverse, and return. 

Second method is more straightforward, and faster as less operation and checks are required. But both algorithm should be O(log(x)) time compexity. 

## 9. Palindrome Number

Three ways

1. First one is just to compare string to reversed string, one line code woo!

2. Second and Third try to only compare half the number, one by math, one by string, but not much improve on time, technically all three are O(log(x))
