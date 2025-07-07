class Solution:
    def maxNumberofBallons(self,text):
        mp = {}
        mp["b"] = 0
        mp["a"] = 0
        mp["l"] = 0
        mp["o"] = 0
        mp["n"] = 0        

        for t in text:
            if t in mp:
                mp[t] += 1
        return min(mp["b"],mp["a"],mp["l"]//2,mp["o"]//2,mp["n"])
if __name__ == "__main__":
    s = Solution()
    print(s.maxNumberofBallons("balloonballoon"))
