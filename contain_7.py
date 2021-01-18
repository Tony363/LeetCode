class Solution:
    def contain7(self,n):
        """count the numbers 1 to n that contains 7"""
        count = 0
        for i in range(6,n+1):
            if "7" in str(i):
                count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.contain7(100))