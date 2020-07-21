def findPairs(self, nums, k):
        c = collections.Counter(nums)
        return  sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)
