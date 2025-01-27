from typing import List
class Solution:
    def plusOne(self, digits: List[int])-> List[int]:
        """
        This function takes a list of integers, where each integer represents a single digit of a number.
        The goal is to add 1 to the number represented by the list and return the updated list of digits.
        
        The solution uses a recursive approach to propagate the carry if adding 1 results in a digit equal to 10.
        """
        def add_carry(index):
            """
            This helper function handles the addition of 1 (and any resulting carry) to the digit at the specified index.
            If adding 1 causes the digit to become 10, it sets the digit to 0 and recursively adds the carry
            to the next significant digit (the one before it).
            
            Args:
                index (int): The current index in the digits list being processed.
            """
            # Base case: If we've gone past the most significant digit, insert 1 at the beginning
            if index < 0:
                digits.insert(0, 1)  # Insert '1' at the start of the list
                return

            # Add 1 to the current digit
            digits[index] += 1

            # Check if there's a carry (i.e., if the digit becomes 10)
            if digits[index] == 10:
                digits[index] = 0  # Reset current digit to 0
                add_carry(index - 1)  # Recursively propagate the carry to the next significant digit

        # Start recursion from the least significant digit (last index)
        add_carry(len(digits) - 1)

        # Return the modified list of digits after adding one
        return digits