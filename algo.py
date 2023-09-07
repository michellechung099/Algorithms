from typing import List

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

# Array 1
# brute force, O(n^2) time complexity
def twoSum(nums, target):
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# two pass hash table O(n)
def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        numMap[nums[i]] = i

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    return []

# one pass hash table O(n)
def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
    return []


# Array 2
# best time to buy and sell stock
def maxProfit(prices):
    left, right = 0, 1
    maxP = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
        else:
            left = right
        right += 1
    return maxP

# Array 3
# contains duplicate
def containsDuplicate(nums: List[int]) -> bool:
    seen = {}

    for num in nums:
        if num in seen and seen[num] >= 1:
            return True
        seen[num] = seen.get(num, 0) + 1
    return False

# Array 4
# product of array except self O(n)
def productExceptSelf(nums: List[int]) -> List[int]:


# Array 5
# maximum subarray
def maxSubArray(nums: List[int]) -> int:


# Array 6
# maximum product subarray


# Array 7
# find min in rotated sorted array


# Array 8
# search in rotated sorted array

# Array 9
# 3 sum


# Array 10
# container with most water


# Two Pointers 1
# Valid Palindrome
def isPalindrome(s):
    cleaned = ''.join(char for char in s.lower() if char.isalnum())
    return cleaned == cleaned[::-1]

# another solution in O(n) time complexity
def isPalindrome(s):
    newStr = ""

    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

# another solution with O(1) memory and O(n) with two pointers
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True

# helper function to determine if the element is alphanum based on ASCII contiguous position
def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
