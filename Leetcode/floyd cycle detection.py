# the brute force approach solution for this would be to use a for loop inside another for loop iterate for i and j through the list and check if i and j are equal if so then return the element at the index.
def duplicates(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    return None

# we can use hashset to optimally implement this to find duplicates in a given list 
def duplicates(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return i
        hashset.add(i)
    return None

# partially correct
# we can initialize 2 pointers slow and fast to increment accordingly and check their corresponding values to find the duplicates
# But using this approach there are few problems with this as it does not fetch duplicates correctly if the elements in the array are positioned in certain way.
def duplicates(nums):
    i = 0
    j = 1
    nums = nums.sort() #  by sorting now the duplicates are adjacent to each other and comparing successive elements will fetch us duplicates
    # due to sorting this will have a time complexity of O(nlogn) and a space complexity of O(n)
    while i < j and j <= len(nums):
        if nums[i] == nums[j]:
            return nums[i]
        i +=1
        j +=1
    return None


#### This is the optimal approach to finding duplicates in a list

# this algorithm is used to detect cycle in a list, and also cycle detection in linked lists
# this helps in finding duplicates in a list as well as linked list, by finding the entrance to the cycle and returning the entry point we can find the duplicate
def cycle(nums):
    tortoise = nums[0]
    hare = nums[0]
    # detecting the intersection of the pointers
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    # detecting the entry point of the cycle
    tortoise = nums[0]
    while tortoise!=hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return hare

nums = [1,2,3,4,5,2,6,7,8]
cycle(nums)