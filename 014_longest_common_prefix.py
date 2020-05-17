class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i in range(len(shortest)):
            c = shortest[i]
            for j in strs:
                print(c, j[i])
                if c != j[i]:
                    return shortest[:i]
        return shortest
