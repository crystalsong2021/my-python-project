"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t,
or false otherwise.

A subsequence of a string is a new string that is formed from the
original string by deleting some (can be none) of the characters without
disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""
"""
*****Solution****
set the lower bound and upper bound
set 2 pointers, one on s and one on t
if you found a match character, increment the s pointer, 
increament the t pointer
if s pointer reach the end of the string, it means, all the character are match
"""


def isSubsequence(s, t):
    s_bound, t_bound = len(s), len(t)
    s_index, t_index = 0, 0

    while s_index < s_bound and t_index < t_bound:
        if s[s_index] == t[t_index]:
            s_index += 1
        t_index += 1
    return s_index == s_bound


result = isSubsequence('bb', 'ahbgdcb')
print(result)
