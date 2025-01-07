# def binary_search(arr, left, right, target):
#     if left <= right:
#         mid = left + (right-left)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             return binary_search(arr, left, mid-1, target)
#         else:
#             return binary_search(arr, mid+1, right, target)
#         return -1
    
def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid]> target:
            right = mid-1
        elif arr[mid] == target:
            return mid
        elif arr[mid]< target:
            left = mid + 1
    return -1

def rotated_sorted_arr(arr, target):
    left  = 0
    right = len(arr)-1
    
    if not arr:
        return -1
    #check if the array is not rotated
    if arr[left] < arr[right]:
        return binary_search(arr, left, right, target)
    
    # finding the pivot element or the max element
    while left <= right:
        mid = left + (right-left)//2
        if arr[left] < arr[mid]:
            left = mid + 1
        else:
            right = mid
    pivot = left
    
    if target<= arr[0]:
        return binary_search(arr, pivot, right, target)
    else:
        return binary_search(arr, left, pivot-1, target)
    return -1