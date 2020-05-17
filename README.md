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
