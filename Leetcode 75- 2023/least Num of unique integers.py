"""
1481. Least Number of Unique Integers after K Removals
Given an array of integers arr and an integer k.
Find the least number of unique integers after removing exactly k elements.


Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s.
1 and 3 will be left.
"""


def findLeastNumOfUniqueInts(arr, k):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    sortedFreq = sorted(freq.items(), key=lambda x: x[1])
    res = len(sortedFreq)

    for key, value in sortedFreq:
        if k >= value:
            k -= value
            res -= 1

    return res


result = findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3)
print(result == 2)
