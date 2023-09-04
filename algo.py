def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        if guess == item:
           return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# brute force, O(n^2) time complexity
def twoSum(nums, target):
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
