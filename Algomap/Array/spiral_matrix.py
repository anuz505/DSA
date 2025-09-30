class Solution:
    def spiralOrder(self, matrix):
        ans = []
        i,j = 0,0
        left,right,down,up = 0,1,2,3
        m = len(matrix)
        n = len(matrix[0])
        direction = right # initial

        left_wall = -1
        right_wall = n
        down_wall = m
        up_wall = 0

        while len(ans) < m * n:
            if direction == right:
                while j < right_wall:
                    ans.append(matrix[i][j])
                    j += 1
                right_wall -= 1
                direction = down
                i,j = i + 1, j - 1
            
            elif direction == down:
                while i < down_wall:
                    ans.append(matrix[i][j])
                    i += 1
                down_wall -= 1
                direction = left
                i,j = i - 1, j - 1

            elif direction == left:
                while j > left_wall:
                    ans.append(matrix[i][j])
                    j -= 1
                left_wall += 1
                direction = up
                i,j = i - 1, j + 1

            elif direction == up:
                while i > up_wall:
                    ans.append(matrix[i][j])
                    i -= 1
                up_wall += 1
                i,j = i + 1, j + 1
                direction = right

        return ans
                     
if __name__ == "__main__":
    s = Solution()
    input = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(input))