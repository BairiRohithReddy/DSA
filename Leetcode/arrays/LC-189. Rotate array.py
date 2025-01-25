class Solution:
    def rotate(self, nums: List[int], k:int) -> None: #type: ignore
        n = len(nums)
        k %= n
        result = []
        for i in range(n):
            result[(i+k)%n] = nums[i]
        nums[:] = result
        
'''
intution:
if k is graeter than n, then we can take k = k % n as the array will be rotated k times and the final result will be same as rotating the array k times.
we can rotate the array by removing the multiples of len of array from k. as the array will be same after rotating n times the length of the array.
Then the new index of each element will be (i+k)%n where n is the length of the array.
so we create a new array and store the elements in the new array at the new index.
then we copy the new array to the original array.
'''
        