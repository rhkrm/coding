class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        dp = [ [0 for _ in nums] for _ in nums]
        for g in range(len(nums)) :
            for i in range(len(nums)-g) :
                j = i+g
                l = nums[i-1] if i>=1 else 1
                r = nums[j+1] if j<len(nums)-1 else 1
                for k in range(i,j+1) :
                    l_burst = dp[i][k-1] if k-1>=i else 0
                    r_burst = dp[k+1][j] if k+1<=j else 0
                    dp[i][j] = max(dp[i][j], l_burst+l*nums[k]*r+r_burst)

        return dp[0][-1]
