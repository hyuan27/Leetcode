# my first solution, compare whole number/string, slow, first one line program on Leetcode! 
class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
 
# second solution, compare only half the number, but still compare string
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = str(x)
        l = len(x)
        if l%2 != 0:
            x = x[:l/2]+x[l/2+1:]
        return x[:l/2] == x[l/2:][::-1]
# third solution, math manipulation
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse*10 + x % 10
            x /= 10
        return x == reverse or x == reverse/10
