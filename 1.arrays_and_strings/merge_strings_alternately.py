"""
1768. Merge Strings Alternately
Solved
Easy
Topics
Companies
Hint
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d


Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

# https://leetcode.com/problems/merge-strings-alternately/submissions/1525057163


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # first try
        """
        word3 = []
        if len(word1) > len(word2):
            maximum, minimum = word1, word2
        else:
            maximum, minimum = word2, word1
        for i in range(len(minimum)):
            word3.append(word1[i])
            word3.append(word2[i])
        if len(word1) != len(word2):
            word3.append(maximum[len(minimum):])
            return ''.join(word3)
        return ''.join(word3)
        """
        # optimized explained
        word3 = []
        # zip function create a iterator as a tuple of iterables pairs, until shorter len
        # iterable.
        for w1, w2 in zip(word1, word2):
            word3.append(w1 + w2)
        # append both remain posibles letters from w1 and w2, when a list of len = n
        # is sliced with a greater index from n will return '' when exceed the index n
        word3.append(word1[len(word2) :])
        word3.append(word2[len(word1) :])
        # ''.join() join '' just as empty space so it doesnt change the str value
        return "".join(word3)
