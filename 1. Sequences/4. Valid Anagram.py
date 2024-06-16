class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS = {}
        for c in s:
            hashS[c] = 1 + hashS.get(c, 0)
        for c in t:
            if c in hashS:
                hashS[c] -= 1
        for c in hashS:
            if hashS[c] != 0:
                return False
        return True

# Link: https://leetcode.com/problems/valid-anagram/