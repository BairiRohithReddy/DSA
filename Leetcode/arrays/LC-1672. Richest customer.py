class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int: #type:ignore
        """
        Calculate the maximum wealth among all customers.

        Wealth is defined as the sum of money in all bank accounts of a customer.

        Args:
        accounts (List[List[int]]): A 2D integer array where accounts[i][j] is the amount of money
                                    the i-th customer has in the j-th bank.

        Returns:
        int: The wealth of the richest customer.

        Approach:
        - Iterate through each customer's accounts.
        - Calculate the total wealth of each customer by summing their account balances.
        - Keep track of the maximum wealth encountered.

        Time Complexity: O(n*m), where n is the number of customers and m is the number of accounts per customer.
        Space Complexity: O(1), as we only use a constant amount of extra space.

        Example:
        Input: accounts = [[1,2,3],[3,2,1]]
        Output: 6
        Explanation: The first customer has wealth 1 + 2 + 3 = 6
                     The second customer has wealth 3 + 2 + 1 = 6
                     Both customers are considered the richest with a wealth of 6 each.
        """
        max_wealth = 0
        for customer_accounts in accounts:
            wealth = sum(customer_accounts)  # Calculate total wealth for current customer
            max_wealth = max(max_wealth, wealth)  # Update max_wealth if current wealth is greater
        
        return max_wealth

# approach -2
# this is simpler but may not be the beginner friendly
        #return max(sum(account) for account in accounts)