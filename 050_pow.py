class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        ret = 1
        while n:
            if n%2 != 0:
                ret *= x
            x *= x
            n = int(n/2)
        return ret
 
 class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        elif n < 0:
            return 1/self.myPow(x, -n)
        elif n%2:
            return x*self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n/2)
