class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m = {}
        global_max = 0
        start = 0
        for i, v in enumerate(s):
            if v in m:
                new_start = m[v] + 1
                if start < new_start:
                    start = new_start
            local_max = i - start + 1
            if global_max < local_max:
                global_max = local_max
            # global_max = max(global_max, i - start + 1) 
            # use max is slower
            m[v] = i
        return global_max
