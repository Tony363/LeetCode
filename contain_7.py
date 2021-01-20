class Solution:
    def contain7(self,n):
        """count the numbers 1 to n that contains 7"""
        count = 0
        for i in range(0,n+1):
            # print(i,end=' ')
            if "7" in str(i):
                count += 1
        return count

    def HM7(self,n):
        count = 0
      
        while n > 0:
            if n % 10 == 7:
                count += 1
            n = n // 10
        return count

    def HM7from1(self,n):
        count = 0
        for i in range(n):
            # print(i,end=" ")
            count += self.HM7(i)
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.contain7(1000))
    print(solution.HM7from1(1000))