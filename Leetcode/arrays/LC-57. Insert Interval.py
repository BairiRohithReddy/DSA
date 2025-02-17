class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: #type:ignore
        """
        Inserts a new interval into a list of non-overlapping intervals and merges if necessary.
        Args:
            intervals (List[List[int]]): A list of non-overlapping intervals sorted by their start times.
            newInterval (List[int]): A new interval to be inserted.
        Returns:
            List[List[int]]: The updated list of intervals after inserting and merging the new interval.
        """
        res = []

        for i in range(len(intervals)):
            # Non-overlapping case (before)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Non-overlapping case (after)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # overlapping case
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval)
        return res
'''
we will iterate through the given array and check if the new interval ends before the start of the next interval if so we append it and return the res
if the newinterval begins after the end of the present interval then we append the present interval and move on
then if wither of these cases fail it means the new interval has a collision 
now we can find the new interval as [min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1])]
then we proceed to check again and then we append this new interval to the result and return

Time and Space Complexity
Time Complexity: O(n) where n is the length of intervals
Space Complexity: O(n) for the result array
'''