"""
JP Morgan HackerRank Q1 (Easy)
Fun with Anagrams
Given an array of strings, remove each string that is an anagram of an earlier string, then return the remaining array in sorted order.

Example
str = ['code', 'doce', 'ecod', 'framer', 'frame']

code and doce are anagrams.
Remove doce from the array and keep the first occurrence code in the array.

code and framer are not anagrams. Keep both strings in the array.
framer and frame are not anagrams due to the extra r in framer. Keep both strings in the array.
Order the remaining strings in ascending order: ['code','frame','framer'].

"""


def isAnagrams(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


def funWithAnagrams(text):
    result = [text[0]]
    for i in range(1, len(text)):
        curr = text[i]
        foundAnagram = False
        for word in result:
            if isAnagrams(word, curr):
                foundAnagram = True
                break
        # if there are no anagram exist in result, then added
        if not foundAnagram:
            result.append(curr)
    return sorted(result)


string = ['code', 'doce', 'ecod', 'framer', 'frame']
string2 = ['code', 'aaagmnrs', 'anagrams', 'doce']
result = funWithAnagrams(string2)
print(result)
