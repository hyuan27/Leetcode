class Solution:
    def numDecodings(self, s: str) -> int:
        
	    if not s:
		    return 0

	    dp = [0 for x in range(len(s) + 1)] 
	
	    # base case initialization
	    dp[0] = 1 
	    dp[1] = 0 if s[0] == "0" else 1   #(1)

	    for i in range(2, len(s) + 1): 
		    # One step jump
		    if int(s[i-1]) != 0:    #(2)
			    dp[i] += dp[i - 1]
		    # Two step jump
		    if 10 <= int(s[i-2:i]) <= 26: #(3)
			    dp[i] += dp[i - 2]
	    return dp[len(s)]
