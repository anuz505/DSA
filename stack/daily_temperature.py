class Solution(object):
    def dailyTemperaturesBruteForce(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break
        return answer
    
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)        
        answer = [0] * n
        stack = []

        for i in range(n):
            if not stack:
                stack.append(i)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop(-1)
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer

if __name__ == "__main__":
    s= Solution()
    input = [73,74,75,71,69,72,76,73]
    print(s.dailyTemperatures(input))
        