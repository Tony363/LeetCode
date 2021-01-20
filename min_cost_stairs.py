class Solution:
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
            print(f1,f2)
        return min(f1, f2)

if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs([0,1,2,2]))