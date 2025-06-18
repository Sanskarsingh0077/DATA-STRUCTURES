class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])

        first_end = points[0][1]

        count = 1 # 1 arrow always needed
        for i in range(1,len(points)):
            if points[i][0] > first_end: # if no overlap increase count
                count +=1
                first_end = points[i][1] #  update first_end
                
        return count # Total Arrows Used 


        '''
        using list


        x = []
        first_end = points[0][1]
        x.append(first_end)

        for i in range(1,len(points)):
            if points[i][0] > first_end:
                first_end = points[i][1]

                x.append(first_end)
        
        return len(x)

        '''