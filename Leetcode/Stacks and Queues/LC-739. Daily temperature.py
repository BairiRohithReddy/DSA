class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: #type:ignore
        '''
        This can be solved using a two pointer approach as follows
        But the below approach has a time complexity of O(n^2) and space complexity of O(n)
        n = len(temperatures)
        res = [0]*n # we are initialising all values to 0 as the min possible value is 0 if no warm temp day is found
        
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break # once a warm day is found we are done
        return res
        The problem can be solved using two approaches
        1. **Brute Force (Two Pointers):**
           - Time Complexity: O(n^2)
           - Space Complexity: O(n)
           - This approach involves iterating through the `temperatures` list 
             using nested loops. The outer loop fixes the current day, and the 
             inner loop searches for the next warmer day. While straightforward, 
             this approach is inefficient for large input sizes.
        
        2. **Optimized Approach (Monotonic Stack):**
           - Time Complexity: O(n)
           - Space Complexity: O(n)
           - This approach utilizes a stack to keep track of the indices of days 
             for which we haven't found a warmer day yet. The stack maintains a 
             decreasing order of temperatures. As we iterate through the 
             `temperatures` list, we compare the current day's temperature with 
             the temperatures at the indices stored in the stack. If we find a 
             warmer day, we update the result for the days in the stack until 
             the stack is empty or the current day is no longer warmer than the 
             top of the stack.
        '''
        
        # Optimized Approach (Monotonic Stack)
        n = len(temperatures)
        res = [0] * n  # Initialize the result array with zeros
        stack = []  # Stack to store indices of days

        for i in range(n):
            # While the stack is not empty and the current temperature is greater 
            # than the temperature at the index at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()  # Get the index of the previous day
                res[prev_i] = i - prev_i  # Calculate the waiting days
            stack.append(i)  # Push the current day's index onto the stack

        return res  # Return the result array