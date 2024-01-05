class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        j =0
        m = len(matrix)
        n = len(matrix[0])
        hor= []
        ver = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j]== 0:
                    hor.append(i)
                    ver.append(j)
        for i in hor:
            for j in range(n):
                if matrix[i][j]!= 0:
                    matrix[i][j]= 0
        for j in ver:
            for i in range(m):
                if matrix[i][j]!= 0:
                    matrix[i][j]= 0
            

        