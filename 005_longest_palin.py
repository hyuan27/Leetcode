# my first solution, O(n^2) time complexity, but space complexity is also O(n^2), could be cleaner...
class Solution(object):
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        m = set()
        m.add('')
        global_max = 0
        longest = ''
        for i in range(len(s)):
            if i == 2 and len(m) == 1:
                return longest
            for j in range(len(s)-i):
                
                sub = s[j:j+i+1]
                if sub in m:
                    continue
                if len(sub) == 1:
                    m.add(sub)
                    global_max = 1
                    longest = sub
                else:
                    if s[j+1:j+i] in m and s[j] == s[j+i]:
                        m.add(sub)
                        global_max = len(sub)
                        longest = sub
        return longest
        
# second solution, still O(n^2), but space complexity is constant

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        result = ''
        for i in range(len(s)):
            temp = self.longest_palindrom(s,i,i)
            if len(temp) > len(result):
                result = temp
            temp = self.longest_palindrom(s,i,i+1)
            if len(temp) > len(result):
                result = temp
        return result
            
            
    # helper to find the longest polindrome from a center        
    def longest_palindrom(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r+= 1
        return s[l+1:r]
  
  # third solution is one that I found online, still O(n^2), but very fast
  class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        max_l = 1
        start = 0
        
        for i in range(1,len(s)):
            if (i-max_l >= 1 and s[i-max_l-1:i+1] == s[i-max_l-1:i+1][::-1]):
                start = i-max_l-1
                max_l += 2
            if (i-max_l >= 0 and s[i-max_l:i+1] == s[i-max_l:i+1][::-1]):
                start = i-max_l
                max_l += 1
        return s[start:start+max_l]
