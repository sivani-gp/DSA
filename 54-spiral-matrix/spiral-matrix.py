class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        colBegin,rowBegin = 0,0
        l=[]
        rowEnd,colEnd = len(matrix)-1,len(matrix[0])-1
        while rowBegin<=rowEnd and colBegin<=colEnd:
            #traverse right
            for j in range(colBegin,colEnd+1,1):
                l.append(matrix[rowBegin][j])
            rowBegin+=1
            #traverse down
            for j in range(rowBegin,rowEnd+1):
                l.append(matrix[j][colEnd])
            colEnd-=1
            #traverse left
            if rowBegin <= rowEnd:
                for j in range(colEnd,colBegin-1,-1):
                    l.append(matrix[rowEnd][j])
                rowEnd-=1
            #traverse up
            if colBegin <= colEnd:
                for j in range(rowEnd,rowBegin-1,-1):
                    l.append(matrix[j][colBegin])
                colBegin+=1
        return l
            