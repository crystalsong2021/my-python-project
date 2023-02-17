"""
5.Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

"""


def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        res1 = len(findPalidome(i, i, s)) > len(res)
        res2 = findPalidome(i, i + 1, s)
    return res


def findPalidome(l, r, s, result):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if r - l + 1 > len(result):
            result = s.slice(l, r + 1)
        l += 1
        r -= 1
    return result


res = longestPalindrome('ababdee')
print(res)
