class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        # sol[][] init 0
        sol = [[0 for col in range(target+1)] for row in range(n+1)]
        
        #init
        for i in range(1,k+1) :
            if i<=target :
                sol[1][i] = 1
                
        
        if n > 1 :
            for nn in range(2,n+1) :
                for tt in range(nn,target+1) :
                    for kk in range(1,k+1) :
                        if tt-kk >= 0 :
                            sol[nn][tt] += sol[nn-1][tt-kk]

            # print(sol)
        
        return sol[n][target] % (10**9 + 7)
        
