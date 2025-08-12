def numberOfWays(self, n: int, x: int) -> int:
        dp = [[-1]*(n+1) for _ in range(n+1)]
        m = 10**9+7
        
        def solve(rem,num):

            if rem == 0:
                return 1

            if n < 0:
                return 0

            if num**x > rem:
                return 0

            if dp[rem][num] != -1:
                return dp[rem][num]


            take = solve(rem-num**x, num+1)
            not_take = solve(rem, num+1)

            dp[rem][num] = (take+ not_take)%m
            return dp[rem][num]

        
        return solve(n,1)
    
'''
    Java Code:
    
    class Solution {
    static final int MOD = 1000000007;
    int dp[][];
    int X;

    public int numberOfWays(int n, int x) {
        this.X = x;
        dp = new int[n+1][n+1];

        for(int i = 0; i<= n ; i++){
            for(int j = 0; j<= n; j++){
                dp[i][j] = -1;
            }
        }

        return solve(n,1);
        
    }

    private int solve(int rem, int num){
        if(rem == 0) return 1;
        
        if(rem<0) return 0;

        if(Math.pow(num,X) > rem) return 0;

        if(dp[rem][num] != -1) return dp[rem][num];

        int take = solve(rem - (int) Math.pow(num,X),num+1);
        int notTake = solve(rem, num+1);

        dp[rem][num] = (int)(((long)take + notTake)%MOD);

        return dp[rem][num];

    }
}
    
    
    '''
    
 