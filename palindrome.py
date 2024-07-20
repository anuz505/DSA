class Solution:
    def __init__(self):
        pass

    def isPalindrome(self, x):
        if x < 0:
            return False

        reverse_number = 0
        temp = x
        while temp != 0:
            m = temp % 10
            reverse_number = reverse_number * 10 + m
            temp //= 10

        return reverse_number == x
       
if __name__ == "__main__":
    n = 121
    number = Solution()
    print(number.isPalindrome(n))
