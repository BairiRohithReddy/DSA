def backtrack(i, n):
    """
    Print numbers from 1 to n using backtracking without incrementing.

    Args:
    i (int): The current number being processed (start with n)
    n (int): The maximum number to be printed

    Returns:
    None
    """
    # Base case: Stop recursion when i becomes less than 1
    if i < 1:
        return
    
    # Recursive case: Move towards the base case
    backtrack(i - 1, n)
    
    # Backtracking step: Print after returning from recursive calls
    print(i)

    # Recursive map for backtrack(5, 5):
    # backtrack(5) -> backtrack(4) -> backtrack(3) -> backtrack(2) -> backtrack(1) -> backtrack(0)
    #     |               |               |               |               |             (returns)
    #     |               |               |               |               prints 1
    #     |               |               |               prints 2
    #     |               |               prints 3
    #     |               prints 4
    #     prints 5

# Example usage:
# backtrack(5, 5)

def backtrack2(i, n):
    """
    Print numbers from n to 1 using backtracking without decrementing.

    Args:
    i (int): The current number being processed (start with 1)
    n (int): The maximum number to be printed

    Returns:
    None
    """
    # Base case: Stop recursion when i becomes greater than n
    if i > n:
        return
    
    # Recursive case: Move towards the base case
    backtrack2(i + 1, n)
    
    # Backtracking step: Print after returning from recursive calls
    print(i)

    # Recursive map for backtrack2(1, 5):
    # backtrack2(1) -> backtrack2(2) -> backtrack2(3) -> backtrack2(4) -> backtrack2(5) -> backtrack2(6)
    #     |               |               |               |               |                 (returns)
    #     |               |               |               |               prints 5
    #     |               |               |               prints 4
    #     |               |               prints 3
    #     |               prints 2
    #     prints 1

# Example usage:
backtrack2(1, 5)