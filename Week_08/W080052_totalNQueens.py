class Solution:
    def totalNQueens(self, n: int) -> int:
        mask = ~((~ 0) << n)
        self.ans = 0

        def dfs(level, cols, pies, nas):  
            if level == n:
                self.ans += 1
                return
            possible = ~(cols | pies | nas) & mask
            while possible:
                next_possible = possible & (possible-1)
                curr_col = possible ^ next_possible
                possible = next_possible
                dfs(level + 1, \
                      cols | curr_col, \
                      (pies | curr_col) << 1, \
                      (nas | curr_col) >> 1 )

        dfs(0, 0, 0, 0)
        return self.ans

