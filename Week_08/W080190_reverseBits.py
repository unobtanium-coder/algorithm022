class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n & 1
            res <<= 1
            res += bit
            n >>= 1
        return res

        # 一行代码：
        # return int("0b"+("0"*32+bin(n)[2:])[-32:][::-1], base=2)
