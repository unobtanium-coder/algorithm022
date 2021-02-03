class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if 0 == n:  return False
        return n & n-1 == 0
