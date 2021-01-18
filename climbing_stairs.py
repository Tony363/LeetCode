class Solution:
    def climbStairs(self, n: int) -> int:
        # len of n is less than 2 there can be only n number of combinations
        if n <=2:
            return n
        # initialize 0 by length of n array
        dp = [0]*n
        # first second element assigned to 1,2
        dp[0] =1
        dp[1] = 2
        # since dp first and second element is assigned loop from 2 to len n
        for i in range(2,n):
            # combination by the ith becomes the ith-1 plus ith-2
            dp[i] = dp[i-1]+dp[i-2]
        print(dp)
        return dp[n-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        # initialize memoized array
        memo = [0] * len(range(n))
        # return the recusion result of climbing stairs
        return self.climb_Stairs(0,n,memo)
    
    def climb_Stairs(self,i,n,memo):
        # if iterator exceeds flight of stairs exit
        if (i>n):
            return 0
        # if iterator is the len of flight of stairs exit with 1 additional combination
        if (i == n):
            return 1
        # if current iterations memoized element is greater than zero, return the memoized element
        if (memo[i]>0):
            return memo[i]
        # calculate current iterations element by future possible iterations combinations
        memo[i] = self.climb_Stairs(i+1,n,memo) + self.climb_Stairs(i+2,n,memo)
        # finally return the the ith memoized element
        return memo[i]