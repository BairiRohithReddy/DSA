class Solution:
    def fizzBuzz(self, n: int) -> List[str]:    #type:ignore
        """
        Generate the FizzBuzz sequence up to n.

        For each number from 1 to n:
        - If the number is divisible by both 3 and 5, append "FizzBuzz"
        - If the number is divisible by 3 (but not 5), append "Fizz"
        - If the number is divisible by 5 (but not 3), append "Buzz"
        - For any other number, append the number itself as a string

        Args:
        n (int): The upper limit of the sequence (inclusive).

        Returns:
        List[str]: A list of strings representing the FizzBuzz sequence.

        Time Complexity: O(n), where n is the input number.
        Space Complexity: O(n) to store the result list.
        """
        
        # Initialize an empty list to store the FizzBuzz sequence
        result = []
        
        # Iterate through numbers from 1 to n (inclusive)
        for i in range(1, n+1):
            # Check if the number is divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            # Check if the number is divisible by 3 (but not 5)
            elif i % 3 == 0 and i % 5 != 0:
                result.append("Fizz")
            # Check if the number is divisible by 5 (but not 3)
            elif i % 5 == 0 and i % 3 != 0:
                result.append("Buzz")
            # For any other number, append the number itself as a string
            else:
                result.append(f"{i}")
        
        # Return the completed FizzBuzz sequence
        return result
