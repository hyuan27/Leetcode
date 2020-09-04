class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i == ')' or i == ']' or i == '}':
                if len(l) == 0 or l[-1] != mapping[i]:
                    return False
                else:
                    l.pop()
            else:
                l.append(i)
        if len(l) == 0:
            return True
        else:
            return False
