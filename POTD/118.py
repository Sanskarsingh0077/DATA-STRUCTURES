def generate(self, numRows: int) -> List[List[int]]:
        result = [[]]*(numRows)

        for i in range(numRows):
            arr = [1]*(i+1)
            result[i] = arr

            for j in range(1, i):
                result[i][j] = result[i-1][j] + result[i-1][j-1]

        return result
