class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in map:
                return [map[remaining],i]
            map[v] = i
