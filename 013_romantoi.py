# first solution
class Solution(object):
    def romanToInt(self, s):
        m = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
        result = 0
        for i in range(len(s)-1):
            if m[s[i]] < m[s[i+1]]:
                result -= m[s[i]]
            else:
                result += m[s[i]]
        return result + m[s[-1]]
        
# second solution
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
