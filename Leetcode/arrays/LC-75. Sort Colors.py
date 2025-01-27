class Solution:
    def sortColors(self, nums: List[int]) -> None: #type: ignore
        left = 0
        mid = 0
        right = len(nums) - 1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                mid +=1
                left +=1
            elif nums[mid] ==1:
                mid +=1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -=1
        return nums
'''
intution:
we are using three pointers left, mid and right.
left is the index of the first 0 in the array.
mid is the index of the current element.
right is the index of the last 2 in the array.
we are iterating through the array using the mid pointer.
if the current element is 0, we swap it with the element at the left pointer and increment both left and mid pointers.
if the current element is 1, we increment the mid pointer.
if the current element is 2, we swap it with the element at the right pointer and decrement the right pointer.

Time complexity: O(n); Space complexity: O(1)
This algorithm is also called as Dutch National Flag algorithm. or three way partitioning. or conting sort.

'''