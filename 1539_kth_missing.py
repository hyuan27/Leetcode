# O(n) solution
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr.insert(0,0)
        for i in range(len(arr)-1):
            if k <= (arr[i+1] - arr[i] - 1):
                return arr[i] + k
            else:
                k -= (arr[i+1] - arr[i] - 1)
        if k != 0:
            return arr[-1] + k
 
 # O(logn) solution, binary search
 class Solution:
    def findKthPositive(self, A, k):
        l, r = 0, len(A)
        while l < r:
            m = int((l + r) / 2)
            print(m)
            if A[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k
