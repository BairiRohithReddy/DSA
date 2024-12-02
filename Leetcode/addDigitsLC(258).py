class Solution:
    def addDigits(self, num: int) -> int:
# Approach 1: Iterative solution
        # This approach repeatedly sums the digits of the number until a single digit is obtained.
        # Time Complexity: O(log(num)) for the inner loop, where log(num) is the number of digits.
        # Space Complexity: O(1) as no additional space is used.

        # Uncomment this block to use the iterative approach
        # while num >= 10:  # Continue while the number has more than one digit
        #     result = 0  # To store the sum of digits
        #     while num > 0:
        #         digit = num % 10  # Extract the last digit
        #         result += digit  # Add the digit to the result
        #         num = num // 10  # Remove the last digit
        #     num = result  # Update num to the sum of its digits
        # return num  # Return the single-digit result
        
# Approach 2: Mathematical solution using the digital root formula
        # The digital root of a number can be calculated in O(1) time.
        # If num == 0, the result is 0.
        # For num > 0, the result is given by 1 + (num - 1) % 9.
        # This formula works because repeatedly summing the digits of a number
        # reduces it to its equivalent mod 9 value.

        if num == 0:
            return 0  # Special case: The digital root of 0 is 0.
        return 1 + (num - 1) % 9  # Digital root formula for non-zero num
