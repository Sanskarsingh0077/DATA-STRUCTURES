class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        
        row = {}

        for i in grid:
            tuple_i =tuple(i)
            row[tuple_i]=row.get(tuple_i,0)+1

        
        for j in range(len(grid[0])):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][j])
            col = tuple(col)
            pairs += row.get(col, 0)
        
        return pairs


        '''
        In- Depth Strategy:
	1.	Use a Hash Map to Track Rows:
	    •	Go through each row in the matrix.
	    •	Convert the row into a tuple (because lists can’t be dictionary keys).
	    •	Store this tuple in a dictionary, where the key is the row, and the value is how many times it appears.
	2.	Iterate Through Each Column:
	    •	For each column index (from 0 to number of columns - 1):
	    •	Construct the column by picking the same index from all rows (i.e., vertical slice).
	    •	Convert the column into a tuple.
	3.	Compare Each Column Tuple to Row Map:
	    •	Check if the current column tuple exists in the row map.
	    •	If it does, it means this column matches one or more rows.
	    •	Add the count of that row from the map to a running total.
	4.	Return the Final Count:
	    •	After checking all columns, return the total count of matching row–column pairs.



        '''