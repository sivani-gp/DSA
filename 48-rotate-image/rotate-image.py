class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range(n//2):
                #store left
                temp = matrix[n-1-j][i]
                #left takes bottom value
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                #bottom takes right
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                #right takes top
                matrix[j][n-1-i] = matrix[i][j]
                #top takes left 
                matrix[i][j] = temp
        return matrix

        