"""
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element
is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

"""


def containDuplicate(numbers):
    hashSet = set()
    for n in numbers:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False


nums = [1, 2, 3, 4]
print(containDuplicate(nums))
