class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of a given 32-bit signed integer.

        Args:
        x (int): The input integer to be reversed.

        Returns:
        int: The reversed integer. Returns 0 if the reversed integer overflows.

        Algorithm:
        1. Initialize result to store the reversed number.
        2. Handle the sign of the input separately by working with its absolute value.
        3. Iterate through each digit of the absolute value:
           a. Extract the last digit.
           b. Add it to the result after shifting existing digits.
           c. Remove the last digit from the input number.
        4. Restore the sign of the number.
        5. Check for 32-bit integer overflow and return 0 if it occurs.

        Time Complexity: O(log|x|), where |x| is the absolute value of x.
                         This is because the number of digits in a number is logarithmic to its value.
        Space Complexity: O(1), as we use only a constant amount of extra space.

        Note: This solution handles the edge cases of negative numbers and 32-bit integer overflow.
        """
        result = 0
        int_max = 2**31 - 1  # Maximum value for a 32-bit signed integer
        int_min = -2**31     # Minimum value for a 32-bit signed integer
        abs_x = abs(x)       # Work with absolute value to simplify reversal process

        while abs_x != 0:
            temp = abs_x % 10     # Extract the last digit
            result = result * 10 + temp  # Shift existing digits left and add new digit
            abs_x //= 10          # Remove the last digit from abs_x

        # Restore the sign of the original number
        result = result if x > 0 else -result

        # Check for 32-bit integer overflow
        if result > int_max or result < int_min:
            return 0

        return result

'''

Time Complexity: O(log|x|)
- The while loop runs for each digit in the number x.
- The number of digits in an integer x is approximately log10|x|.
- Each operation inside the loop (modulo, multiplication, division) is O(1) for standard integer sizes.
- Therefore, the overall time complexity is O(log|x|).

Space Complexity: O(1)
- The algorithm uses a fixed number of variables (result, int_max, int_min, abs_x, temp) regardless of the input size.
- These variables don't grow with the input size.
- Hence, the space complexity is constant, O(1).

Additional Analysis:
1. The operations int_max = 2**31 - 1 and int_min = -2**31 are O(1) as they're constant time computations.
2. The final comparison (result > int_max or result < int_min) is also O(1).
3. The sign restoration (result if x > 0 else -result) is a constant time operation.

'''