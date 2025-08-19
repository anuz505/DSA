# lets write a log2n solution
class Solution:
    def perfectSquare(self,num):
        if num < 0:
            return False
        if num == 0 or num ==1:
            return True
        l = 0
        r = num

        while l <=r:
            m = (l + r) // 2
            square = m * m
            
            if (square ) == num:
                return True
            elif (square)> num:
                r = m - 1
            else:
                l = m + 1
        return False
    
if __name__ == "__main__":
    S = Solution()
    num = int(16)
    res = S.perfectSquare(num)
    print(res)
