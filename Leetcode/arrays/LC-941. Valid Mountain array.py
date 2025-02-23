class Solution:
    def validMountainArray(self, arr: List[int]) -> bool: #type:ignore
        if len(arr)<3 or not arr:
            return False
        i = 0
        while i<len(arr)-1 and arr[i]<arr[i+1]:
            i+=1
        if i==0 or i==len(arr)-1:
            return False
        while i<len(arr)-1 and arr[i]>arr[i+1]:
            i +=1
        return i == len(arr)-1
    # in a single pass we can find if the given array is valid or not
    # time complexity = O(n)
    # space complexity = O(1) 
    
    # or we can also use this approach 
    # if len(arr) < 3 or not arr:
    #     return False
        
    # max_idx = 0
    # for i in range(1, len(arr)):
    #     if arr[i] <= arr[max_idx]:
    #         break
    #     max_idx = i
        
    # if max_idx == 0 or max_idx == len(arr) - 1:
    #     return False
        
    # for i in range(max_idx, len(arr) - 1):
    #     if arr[i] <= arr[i + 1]:
    #         return False
        
    # return True