class Solution(object):
    def isPalindrome(self, s):
        """
        O(n)
        :type s: str
        :rtype: bool
        """
        filtered = "".join(c for c in s if c.isalnum())
        filtered = filtered.lower()
        reversed = filtered[::-1]
        if s == reversed:
            return True
        else:
            return False
        
    def isPalindromeTwoPointer(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## O(n)
        n = len(s)
        l = 0
        r = n-1
        while l < r:
            if not s[l].isalnum():
                l+=1
                continue

            if not s[r].isalnum():
                r-=1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1

        return True
        

if __name__ == "__main__":
    S = Solution()
    print(S.isPalindrome(""))