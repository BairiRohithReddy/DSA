class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]: #type:ignore
        n = len(heights)
        res = [0] * n  # Initialize the result list with zeros
        stack = []  # Initialize an empty stack to keep track of visible people
        
        # Iterate through the heights list from the end to the beginning
        for i in range(n - 1, -1, -1):
            count = 0  # Initialize the count of visible people for the current person
            
            # Pop from the stack until the current person's height is greater than the height of the person on top of the stack
            while stack and heights[i] > stack[-1]:
                count += 1
                stack.pop()
            
            # If the stack is not empty, the current person can see one more person (the one on top of the stack)
            if stack:
                count += 1
            
            res[i] = count  # Store the count in the result list
            stack.append(heights[i])  # Push the current person's height onto the stack
        
        return res
    '''
    Time Complexity: (O(n))
    Space Complexity: (O(n))
    '''