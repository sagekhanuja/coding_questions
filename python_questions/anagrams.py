"""
Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

"""
import collections

def groupAnagramWords(strs):
    output = {}
    for word in strs:
        if ''.join(sorted(word)) in output.keys():
            output[''.join(sorted(word))].append(word)
        else:
            output[''.join(sorted(word))] = [word]
    return list(output.values())


print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]