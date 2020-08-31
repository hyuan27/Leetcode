class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        k = 1
        count = 0
        while N-k*(k+1)/2 >= 0:
            if (N-k*(k+1)/2)%k == 0:
                count+=1
            k += 1
        return count
