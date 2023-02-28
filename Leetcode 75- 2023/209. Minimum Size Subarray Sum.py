"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
[2, 3, 1, 2, 4, 3]
             l
                r
*****important*** using 2 while loop - because we want the left pointer to catch up to meet the requirement
"""


def minSubArray(nums, target):
    l, r, total, min_length = 0, 0, 0, 0
    while r < len(nums):
        total += nums[r]
        while total >= target:
            length = r - l + 1
            if min_length == 0 or length < min_length:
                min_length = length
            # let the left pointer move forward
            total -= nums[l]
            l += 1
        r += 1
    return min_length


res = minSubArray([2, 3, 1, 2, 4, 3], 7)
print('Result: ', res)
