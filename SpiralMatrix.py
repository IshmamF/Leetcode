# Problem: https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visit = set()
        spiral_values = []
        rows = len(matrix)
        cols = len(matrix[0])

        def helper(r, c):
            if (r, c) in visit or r >= rows or r < 0 or c >= cols or c < 0:
                return

            visit.add((r, c))

            spiral_values.append(matrix[r][c])

            helper(r, c + 1)
            helper(r + 1, c)
            helper(r, c - 1)
            helper(r - 1, c)

        helper(0, 0)
        return spiral_values
# Depth first search made the most sense since we're going to the end of the column, then all the way to the bottom within the same column
# then all the way to the left, and then all the way up
# Base case is that revisit the same position or go out of bounds, and in those cases, you don't return anything
# Time complexity = O(4^nm), Space Complexity = O(n * m) 
# n = number of rows, m = number of columns
    
