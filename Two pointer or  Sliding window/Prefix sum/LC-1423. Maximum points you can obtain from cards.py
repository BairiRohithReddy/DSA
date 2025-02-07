class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int: # type:ignore
        max_score = sum(cardPoints[:k])
        curr_score = max_score
        n = len(cardPoints)-1
        
        for i in range(k):
            curr_score = curr_score -cardPoints[k-i-1] + cardPoints[n-i]
            max_score = max(max_score, curr_score)
        return max_score
        '''
        We can solve this problem by using sliding window technique.
        We will calculate the sum of the first k elements and store it in max_score.
        We will also store the current score in curr_score.
        We will iterate over the array from k-1 to 0.
        We will update the curr_score by subtracting the kth element and adding the last element.
        We will update the max_score by taking the maximum of max_score and curr_score.
        Finally we will return max_score.
        time complexity: O(N)
        space complexity: O(1)
        '''