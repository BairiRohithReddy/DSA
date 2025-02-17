class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: #type:ignore
        intervals.sort(key=lambda x:x[0])
        res = []
        start = intervals[0]
        for i in range(len(intervals)):
            if intervals[i][0] > start[0]:
                res.append(start)
                start = intervals[i]
            else:
                start = [
                    min(start[0], intervals[i][0]),
                    max(start[1], intervals[i][1])
                ]
        res.append(start)
        return res