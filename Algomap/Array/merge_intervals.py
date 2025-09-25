class Solution:
    def mergeIntervals(self,intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_intervals = sorted(intervals)
        final_intervals= []
        for i in range(len(sorted_intervals)):
            if not final_intervals or final_intervals[-1][1] < sorted_intervals[i][0]:
                final_intervals.append(sorted_intervals[i])
            else:
                final_intervals[-1][1] = max(final_intervals[-1][1],sorted_intervals[i][1])
        return final_intervals
if __name__ == "__main__":
    S = Solution()
    print(S.mergeIntervals([[2,6],[1,3],[8,10],[7,9]]))