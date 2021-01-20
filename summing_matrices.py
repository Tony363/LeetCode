import numpy as np

class Solution:
    def r_start(self,i):
        return max(0, i-self.K)
    
    def r_end(self,i):
        return min(i+self.K+1,self.m)
    
    def c_start(self,j):
        return max(0,j-self.K)
    
    def c_end(self,j):
        return min(j+self.K+1,self.n)
    
    def matrixBlockSum1(self, mat: List[List[int]], K: int) -> List[List[int]]:
        self.mat = mat
        self.K = K
        self.m = len(mat)
        self.n = len(mat[0])
        matrix = np.asarray([[0 for j in range(self.n)] for i in range(self.m)])
        for i in range(self.m):
            for j in range(self.n):
                matrix[i][j] = sum([sum([mat[r][c] for c in range(self.c_start(j),self.c_end(j))]) for r in range(self.r_start(i),self.r_end(i))])
                
        return matrix
    
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        matrix = np.asarray([[0 for j in range(len(mat[0]))] for i in range(len(mat))])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                r_start = max(0, i-K)
                r_end = min(i+K+1,len(mat))
                c_start = max(0,j-K)
                c_end = min(j+K+1,len(mat[0]))
                result = sum([sum([mat[r][c] for c in range(c_start,c_end)]) for r in range(r_start,r_end)])
                matrix[i][j] = result
        return matrix