class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)

        maxArea = 0.0

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    x1 = points[i][0]
                    y1 = points[i][1]

                    x2 = points[j][0]
                    y2 = points[j][1]

                    x3 = points[k][0]
                    y3 = points[k][1]


                    shoelace = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) #Shoelace Formula for Area of a triangle.

                    maxArea = max(maxArea,shoelace)


        return maxArea