class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [ [ False for i in range(len(s)) ] for j in range(len(s)) ]
        res = s[0]
        max_len = 1
        
        for i in range(len(s)) :
            dp[i][i] = True
        
        for j in range(1,len(s)) :
            for i in range(j) :
                if s[i] == s[j] :
                    if j-i == 1 or dp[i+1][j-1] :
                        dp[i][j] = True
                        if j-i+1 > max_len :
                            res = s[i:j+1]
                            max_len = j-i+1           
    
        
        return res
