class Solution:
    def smallestNumber(self, n: int) -> int:
        """
        Find the smallest number that is greater than or equal to n and is of the form 2^k - 1.

        Intuition:
        The smallest number >= n of the form 2^k - 1 will have all bits set to 1
        up to the most significant bit of n, and possibly one more.

        Idea:
        1. Find the position of the most significant bit in n.
        2. Create a number with a 1 in the next bit position.
        3. Subtract 1 from this number to get all 1s in the lower bits.

        Args:
        n (int): The input number.

        Returns:
        int: The smallest number >= n that is of the form 2^k - 1.

        Time Complexity: O(1), as bit operations are constant time.
        Space Complexity: O(1), using only a constant amount of extra space.
        """
        
        # Get the number of bits needed to represent n
        k = n.bit_length()
        
        # Create a number with 1 in the (k+1)th position: 2^k
        power_of_two = 1 << k
        
        # Subtract 1 to get k ones: 2^k - 1
        return power_of_two - 1

        # Alternative implementation:
        # if n & (n+1) == 0:
        #     # If n is already of the form 2^k - 1, return n
        #     return n
        # temp = n
        # # "Smear" the bits to the right
        # temp |= temp >> 1  # Copy highest 1 bit to the right
        # temp |= temp >> 2  # Copy highest 2 bits to the right
        # temp |= temp >> 4  # Copy highest 4 bits to the right
        # temp |= temp >> 8  # Copy highest 8 bits to the right
        # temp |= temp >> 16  # Copy highest 16 bits to the right
        # temp |= temp >> 32  # For 64-bit integers
        # return temp
