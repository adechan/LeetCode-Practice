# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        save_rows = []
        for i in range(0, len(matrix)):
            save_rows.append(matrix[i].copy())

        save_cols = []
        for i in range(0, len(matrix)):
            save_col = []
            for j in range(0, len(matrix)):
                save_col.append(save_rows[j][i])
            save_cols.append(save_col)

        print(save_cols)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                matrix[j][i] = save_cols[j][len(matrix) - 1 - i]

        return matrix

s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2], [3, 4]]
print(s.rotate(matrix))
