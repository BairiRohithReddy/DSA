class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # To track numbers we've seen to avoid cycles
        while n != 1 and n not in visited:
            visited.add(n)  # Mark current number as seen
            result = 0
            while n > 0:
                digit = n % 10  # Extract the last digit
                result += digit * digit  # Add square of digit to result
                n //= 10  # Remove last digit
            n = result  # Update n to the sum of squares
        return n == 1  # If n == 1, it's a happy number.
