class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix=[]
        m,n=len(matrix),len(matrix[0])
        self.prefix=[[0]* (n+1) for r in range(m+1)]
        for r in range(m):
            total=0
            for c in range(n):
                total+=matrix[r][c]
                self.prefix[r+1][c+1]=total+self.prefix[r][c+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        aboveS=self.prefix[row1][col2+1]
        leftS=self.prefix[row2+1][col1]
        lower=self.prefix[row2+1][col2+1]+self.prefix[row1][col1]-aboveS-leftS
        return lower

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
