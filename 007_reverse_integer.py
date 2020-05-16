# Solution use only math
class Solution(object):
    def reverse(self, x):
        result = 0
        negative = False
        l = []
        if x < 0:
            negative = True
            x = -x
        while x > 0:
            div, rem = divmod(x,10)
            x = div
            l.append(rem)
            multiplier = 1
        for i in range(len(l)-1, -1,-1):
            print(l[i])
            result += (l[i]*multiplier)
            multiplier *= 10
        if result > 2**31 - 1:
            return 0
        if negative:
            return result*-1
        return result
        
# solution that use string manipulation

class Solution(object):
    def reverse(self, x):
        if x < 0:
            x = -int(str(-x)[::-1])
        else:
            x = int(str(x)[::-1])
        if abs(x) > 2 ** 31 - 1:
            return 0
        return x
