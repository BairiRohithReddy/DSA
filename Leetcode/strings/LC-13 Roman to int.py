class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.

        This method presents two approaches to solve the problem, each with its own logic and considerations.

        Args:
            s (str): A string representing a Roman numeral.

        Returns:
            int: The integer value of the Roman numeral.
        """
        # Dictionary mapping Roman symbols to their integer values
        m = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        
        # Approach 1: Iterating up to the second-to-last character
        """
        for i in range(len(s)-1):
            if m[s[i]] < m[s[i+1]]:
                result -= m[s[i]]
            else:
                result += m[s[i]]
        result += m[s[-1]]  # Add the value of the last character
        return result
        """

        # Approach 2: Iterating through all characters
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                result -= m[s[i]]
            else:
                result += m[s[i]]
        return result

        """
        Differences and Reasoning:

        1. Iteration Range:
           - Approach 1: Iterates up to len(s)-1, excluding the last character.
           - Approach 2: Iterates through all characters.
           Reason: Approach 1 handles the last character separately to avoid index out of range errors when comparing with the next character.

        2. Handling the Last Character:
           - Approach 1: Adds the last character's value after the loop.
           - Approach 2: Includes the last character in the main loop logic.
           Reason: Approach 2 simplifies the code by treating all characters uniformly within the loop.

        3. Comparison Logic:
           - Both approaches use the same core logic of comparing adjacent characters.
           - If a smaller value precedes a larger value, it's subtracted; otherwise, it's added.

        4. Error Prevention:
           - Approach 1: Avoids potential index errors by not accessing s[i+1] for the last character.
           - Approach 2: Uses an additional condition (i < len(s) - 1) to prevent index out of range errors.

        Conclusion:
        We arrived at these approaches through iterative problem-solving:
        1. Initially, we recognized the need to compare adjacent characters in Roman numerals.
        2. Approach 1 was developed to handle this comparison safely by excluding the last character from the loop.
        3. Approach 2 evolved as an optimization, aiming to include all characters in a single loop while still preventing errors.
        4. Both approaches are valid and correct, with Approach 2 being slightly more concise and potentially more intuitive.

        The choice between these approaches might depend on personal preference or specific requirements for code readability and structure.
        """