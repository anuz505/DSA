class Solution:
    def MergeStrings(self, word1,word2):
        s = []
        a,b = 0 , 0
        A,B = len(word1),len(word2)
        word = 1
        while a < A and b< B:
            if(word == 1):
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1
        while a < A:
            s.append(word1[a])
            a += 1
        while b<B:
            s.append(word2[b])
            b += 1
        return ''.join(s)

if __name__ == '__main__':
    S = Solution()
    print(S.MergeStrings('abc','defggh')) #adbecf
            