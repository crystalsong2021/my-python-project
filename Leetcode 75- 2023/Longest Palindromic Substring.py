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
        res = len(findPalidome(i, i, s)) > len(res)
        findPalidome(i, i+1, s)


def findPalidome(l, r, s, res):

    while (l >=0 and r < len(s) and s[l] == s[r]):
        if r-l+1 > len(res):
            res = s.slice(l, r+1)
        l+=1
        r-=1
    return res
