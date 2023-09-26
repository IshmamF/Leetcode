# Problem : https://leetcode.com/problems/search-a-2d-matrix-ii/description/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])
        q = []
        q.append((0,0))
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        visit = set()
        visit.add((0,0))
        heapq._heapify_max(q)

        while q:
            row,col = heapq._heappop_max(q)

            if matrix[row][col] == target:
                return True

            for dx,dy in directions:
                r = row + dx
                c = col + dy

                if r in range(ROWS) and c in range(COLS) and (r,c) not in visit:
                    if matrix[r][c] <= target:
                        heapq.heappush(q,(r,c))
                        visit.add((r,c))

        return False
# this solution is ineffecient since the rows and columns are sorted a binary search through each array would've saved time and space.
# My solution would be O(4^nm) time complexity since the target value could be really big and near the end of the matrix, the algorithm
# would be checking 4 directions for every row and column. Space Complexity would be O(n) because of the visit set() 
# I utilized this solution to brush up on bfs and traversing a grid

# Alternative solution with O(n) time complexity and O(1) space complexity:
        for Row in matrix:
            if target in Row:
                return True
        return False
