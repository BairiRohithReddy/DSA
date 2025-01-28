class Solution:
    def dayofYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days[1] = 29
        return sum(days[:month-1]) + day
    
'''
intution:
we are using the days array to store the number of days in each month.
if the year is a leap year, we are changing the number of days in february to 29.
we are using the sum function to get the sum of the days in the months before the given month and adding the day of the month to get the total number of days.
time complexity: O(1)
space complexity: O(1)
additional space: O(1)
another approach is to use the datetime module to get the day of the year.
like this:
import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        return datetime.datetime.strptime(date, '%Y-%m-%d').timetuple().tm_yday
the above approach is also O(1) time and space complexity.
'''
