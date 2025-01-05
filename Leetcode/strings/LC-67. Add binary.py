class Solution:
    """
    A class used to represent the solution for adding two binary strings.
    Methods
    -------
    addBinary(a: str, b: str) -> str
        Adds two binary strings and returns their sum as a binary string.
    """
    """
        Adds two binary strings and returns their sum as a binary string.
        Parameters
        ----------
        a : str
            The first binary string.
        b : str
            The second binary string.
        Returns
        -------
        str
            The sum of the two binary strings as a binary string.
        Approach
        --------
        The function uses a two-pointer technique to traverse both strings from the end to the beginning.
        It maintains a carry to handle the sum of bits that exceed 1 (binary addition).
        The result is built in reverse order and then reversed at the end to get the correct binary sum.
        Intuition
        ---------
        Binary addition is similar to decimal addition but with base 2. The carry is propagated to the next higher bit.
        By starting from the least significant bit (end of the string), we can easily manage the carry and build the result.
        Asymptotic Analysis
        -------------------
        Time Complexity: O(max(N, M)), where N and M are the lengths of the input strings a and b, respectively.
        Space Complexity: O(max(N, M)), for storing the result.
    """
    def addBinaryOptimized(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns their sum as a binary string.
        Args:
            a (str): The first binary string.
            b (str): The second binary string.
        Returns:
            str: The sum of the two binary strings as a binary string.
        Example:
            >>> addBinaryOptimized("1010", "1011")
            '10101'
        The function works by:
            1. Converting the binary strings to integers.
            2. Adding the integers.
            3. Converting the sum back to a binary string.
            4. Removing the '0b' prefix from the binary string representation.
        """
        # Convert binary strings to integers
        num1 = int(a, 2)
        num2 = int(b, 2)
        '''
            a = int(a,2)
            This line converts the binary string a to an integer. 
            The int() function with a base of 2 interprets the string as a binary number.
            b = int(b,2)
            Similarly, this converts the binary string b to an integer.
            result = a + b
            Now that we have both numbers as integers, we can simply add them using standard integer addition.
            return bin(result)[2:]
            This final line does two things:
            bin(result) converts the integer sum back to a binary string representation.
            The [2:] slice removes the first two characters of the binary string, which are always '0b' (indicating it's a binary number).
        '''
        # Sum the integers
        total = num1 + num2
        
        # Convert the sum back to a binary string
        return bin(total)[2:]
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        i,j = len(a)-1, len(b)-1

        while i >=0 or j >= 0 or carry:
            sum_bin = carry
            if i>=0:
                sum_bin += int(a[i])
                i -= 1
            if j>=0:
                sum_bin += int(b[j])
                j -= 1
            result.append(str(sum_bin % 2))
            carry  = sum_bin // 2
        return ''.join(result[::-1])