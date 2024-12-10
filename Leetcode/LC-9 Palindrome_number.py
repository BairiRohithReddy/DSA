class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if a given integer is a palindrome.

        A palindrome is a number that reads the same backwards as forwards.

        Args:
            x (int): The integer to check.

        Returns:
            bool: True if the number is a palindrome, False otherwise.
        """
        # If the number is negative, it can't be a palindrome
        if x < 0:
            return False

        # Initialize variables
        req_number = 0  # Will store the reversed number
        temp = x        # Temporary variable to manipulate without modifying x

        '''
        now we will extract one digit after the other from the given number by
        taking modulo with 10 which gives us the last digit of the number, further dividing this
        number with 10 and performing modulo with 10 will yield the remaining 2 digits
        now upon extracting the first digit we will construct the required number using
        req_number = req_number * 10 + digit
        this will essentially reverse the given number 
        once the number is constructed the temp will finally become 0 and exit the while loop
        then we will check if the constrcuted number is equal to the given number and return it 
        '''
        # Reverse the number
        while temp != 0:
            # Extract the last digit
            digit = temp % 10
            
            # Add the digit to req_number
            req_number = req_number * 10 + digit
            
            # Remove the last digit from temp
            temp //= 10

        # Check if the reversed number is equal to the original
        return req_number == x