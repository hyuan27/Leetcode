# my solution, recursion with memoization. 
m = {}
m[1] = 1
m[2] = 2
class Solution(object):
    def climbStairs(self, n):
        if n in m:
            return m[n]
        else:
            m[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return m[n]

# solution online, super short!
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
