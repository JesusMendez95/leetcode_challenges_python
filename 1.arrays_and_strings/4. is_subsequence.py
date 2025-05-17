""" Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code? """

# len s <= len t


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 or (len(s) == 0 and len(t) == 0):
            return True
        if len(s) > len(t) or len(t) == 0:
            return False
        i = 0
        j = 0
        t_sublist = []
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                t_sublist.append(t[i])
                i += 1
                j += 1   
            else:
                i += 1
        if s == ''.join(t_sublist):
            return True
        else:
            return False

solution = Solution()
print(solution.isSubsequence(s='axc', t='ahbgdc'))

                

