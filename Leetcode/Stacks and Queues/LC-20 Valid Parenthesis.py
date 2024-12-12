class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in s:
            if i == "(":
                temp.append(")")

            elif i == "[":
                temp.append("]")

            elif i == "{":
                temp.append("}")
            elif not temp or i != temp.pop():
                return False

        return len(temp)==0
'''
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string has valid parentheses.

        This method checks if the given string contains valid pairs and ordering of parentheses.
        It uses a stack-based approach to match opening and closing brackets.

        Args:
            s (str): A string containing parentheses characters: '(', ')', '{', '}', '[', ']'

        Returns:
            bool: True if the parentheses in the string are valid, False otherwise.

        Algorithm:
        1. Iterate through each character in the string.
        2. If it's an opening bracket, push its corresponding closing bracket onto the stack.
        3. If it's a closing bracket, check if it matches the top of the stack.
        4. After processing all characters, check if the stack is empty.
        """

        # Initialize an empty list to use as a stack
        stack = []

        # Iterate through each character in the input string
        for char in s:
            if char == "(":
                # For opening parenthesis, push its closing counterpart
                stack.append(")")
            elif char == "[":
                # For opening square bracket, push its closing counterpart
                stack.append("]")
            elif char == "{":
                # For opening curly brace, push its closing counterpart
                stack.append("}")
            else:
                # For closing brackets, check if they match the expected closing bracket
                if not stack or char != stack.pop():
                    # If stack is empty (no opening bracket) or 
                    # the current char doesn't match the top of the stack,
                    # the parentheses are invalid
                    return False

        # After processing all characters, the stack should be empty for valid parentheses
        return len(stack) == 0

        """
        Explanation of the approach:

        1. Stack Usage:
           - We use a list (stack) to keep track of expected closing brackets.
           - This allows us to handle nested parentheses effectively.

        2. Handling Opening Brackets:
           - When an opening bracket is encountered, we push its corresponding closing bracket onto the stack.
           - This prepares us for what we expect to see later in the string.

        3. Handling Closing Brackets:
           - When a closing bracket is encountered, we check two things:
             a. Is the stack empty? If so, we have a closing bracket without a matching opening bracket.
             b. Does it match the top of the stack? If not, we have mismatched brackets.
           - If either condition is true, we return False immediately.

        4. Final Check:
           - After processing all characters, we check if the stack is empty.
           - An empty stack means all opening brackets were properly closed.
           - Any remaining items in the stack indicate unclosed opening brackets.

        5. Time and Space Complexity:
           - Time Complexity: O(n), where n is the length of the string.
           - Space Complexity: O(n) in the worst case, where all characters are opening brackets.

        This approach efficiently handles various cases of nested and sequential parentheses,
        ensuring both proper pairing and correct ordering of different types of brackets.
        """
'''