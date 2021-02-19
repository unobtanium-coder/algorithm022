class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        dict = [0 for _ in range(256)]
        for ch in s:
            dict[ord(ch)] += 1
        for i in range(len(s)):
            ch = s[i]
            if dict[ord(ch)] == 1: return i
        return -1
