class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = []
        for index, char in enumerate(s):
            if char == '(':
                l.append(index)
            if char == ')':
                if len(l) == 0:
                    s = s[:index] + 'X' + s[index + 1:]
                else:
                    l.pop()
        if len(l) != 0:
            for index in l:
                s = s[:index] + 'X' + s[index + 1:]
        s = s.replace('X', '')
        return s
