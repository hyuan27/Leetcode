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

## 5. Longest Palindromic Substring

DP question: 

1. Classic DP, store information as we go, build up from short substrings to longs

2. Still O(n^2) time, but space complexity is now constant

3. Still O(n^2) but very fast. The idea is that every character we add, we at most add 1 or 2 length to the longest palindrme. very cool idea. 

## 7. Reverse Integer:

Two ways

1. Use module and divide to find each digit and reverse, slow

2. Change to string, reverse, and return. 

Second method is more straightforward, and faster as less operation and checks are required. But both algorithm should be O(log(x)) time compexity. 

## 9. Palindrome Number

Three ways

1. First one is just to compare string to reversed string, one line code woo!

2. Second and Third try to only compare half the number, one by math, one by string, but not much improve on time, technically all three are O(log(x))

## 11. Container With Most Water

Two Ways: 

1. Of course we can brute force, O(n^2)

2. But a better O(n) exist, idea being that we first select the wildest as a starting candidate, then moving inward, since only the shorter line of the two lines at boundary matters, we will move the shorter line once, and check if the water contained can be more than before. With less width, only increasing length of the shorter boundary helps. 


## 13. Roman to Integer

Two ways: Both O(n)

1. One approach is conditioning, if we see a letter that represents a smaller number is in front of a letter that represents a bigger number, then we distract it. Else we add it

2. Manipulate the string so we always add, for example, IV could be written as IIII, IX could be written as VIIII, weird method but seems to be faster

## 14. Longest Common Prefix

Three different ways: 

1. Horizontal search, compare pair by pair, O(S)

2. Vertical search, compare all strings, char by char O(S), S is amount of characters in all strings

3. Binary search, idea is to find a string, split in half, and search in all other strings, but slower, O(S*logm), m is the length of the string being compared.

## 20. Valid Parentheses

Using stacks again, O(n)

## 50. Pow(x, n)

Best is O(logn), can do it in both iterative and recursive. 

## 70. Climbing Stairs

Basically just a Fibonacci:

Use Memoization to turn a O(2^n) recursion algorithm to a O(n) algorithm. 

Two other methods have O(logn) time:

One is binet's method, claims that the Fn = Q^n-1[0,0], where Q = [[1,1],[1,0]], the initial condition. If we multiply matrix just one by one, still O(n), but if we represent a matrix multiplication with a tree, then we can do it in log(n) time. 

Another has close form solution 

## 91. Decode Ways

DP problem, running time is O(n). Storage is also O(n) in this code, but could easily reduce to O(1)

## 429. N-ary Tree Level Order Traversal:

Very standard BFS, linear time

## 532. K-diff Pairs in Array

Use a counter in case k = 0, when k >0, just use in method, O(n)

## 547. Friend Circles

DFS, running time is O(n^2), n is the number of people

## 780. Reaching Points

Idea is to go from the destination to the starting point, by using module. O(logN) and N is the maximum of tx and ty

## 796. Rotate String

The O(n^2) method is very easy to do, but there are clean one line versions

The O(n) method using hash function require lots of modula arithmetic background in implementation, could be tough to write. But indeed faster

## 829. Consecutive Number Sum

O(sqrt(N)) time. Trick is to use math to figure out that if N = x + x+1 + x+2 + x+k-1, k >=1, then N = k*x + k(k-1)/2, and then figure out N-k(k-1)/2 must can evenly divide k, and try k from 0.

## 993. Cousins in Binary Tree:

Can do this both use DFS and BFS, BFS achieve slightly better running time as it checks level by level, have bigger chance of stopping early. 
But both have worst case O(n) linear time. And also uses linear space. 

## 1041. Robot Bounded In Circle:
Idea is that if after the sequence, it is either back at origin, or facing a different direction then north, then it will come back to the origin eventually(in 1 or 3 iterations). Time is O(n) 

## 1249. Minimum Remove to Make Valid Parentheses:

Basic idea is to use a stack, the running time is O(n)

## 1539. Kth Missing Positive Number:

Binary Search is the best approach, O(logn) time with O(1) space
