class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n = len(dimensions)

        maxDiag = 0
        maxArea = 0
        
        for i in range(n):
            l = dimensions[i][0]
            w = dimensions[i][1]

            diag = l*l + w*w
            area = l * w

            if diag > maxDiag:
                maxDiag = diag
                maxArea = area

            elif diag == maxDiag:
                maxArea = max(maxArea, area)


        return maxArea