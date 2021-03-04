# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
#
# Follow up:
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    def setZeroes(self, matrix) -> None:
        rows = len(matrix)
        columns = len(matrix[0])

        save_rows = []
        for i in range(0, rows):
            save_rows.append(matrix[i].copy())

        for i in range(0, rows):
            for j in range(0, columns):
                if save_rows[i][j] == 0:
                    # change rows
                    for k in range(0, len(matrix[0])):
                        matrix[i][k] = 0

                    # change columns
                    for k in range(0, len(matrix)):
                        matrix[k][j] = 0

        return matrix

s = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(s.setZeroes(matrix))