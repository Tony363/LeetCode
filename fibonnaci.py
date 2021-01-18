class Solution:
    def fib(self, n: int) -> int:
        # if n is 0
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # initialize memoized array
        fibonacci = [0,1]
        # initialize i
        incre = 2
        # while incre less than n
        while incre <= n:
            # calculate current iteration number
            number = fibonacci[incre-1] + fibonacci[incre-2]
            if incre == n:
                return number
            fibonacci.append(number)
            incre += 1
        return 

    @staticmethod
    def fib2(n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return Solution.fib2(n - 1) + Solution.fib2(n - 2)

        

if __name__ == '__main__':
    # print(Solution.fib2(100))
    solution = Solution()
    print(solution.fib(100))
    