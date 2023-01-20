"""
# 1480 Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i]
= sum(nums[0]...nums[i])

Return the running sum of nums.
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

"""


def runningSum(nums):
    total_sum = 0
    for i in range(len(nums)):
        total_sum = total_sum + nums[i]
        nums[i] = total_sum

    return nums


print(runningSum([1, 2, 3, 4]))
