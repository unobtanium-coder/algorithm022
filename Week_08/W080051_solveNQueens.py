class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mask = ~((~ 0) << n)
        ans = []

        # 参数sol为str型，依次放棋盘最上方level行已解出皇后所在列数，列数从最右0列向左递增计数
        def dfs(sol, level, cols, pies, nas):  
            if level == n:
                ans.append(sol)
                return
            possible = ~(cols | pies | nas) & mask
            while possible:
                next_possible = possible & (possible-1)
                curr_col = possible ^ next_possible
                possible = next_possible
                dfs(sol + chr(45 + len(bin(curr_col))), level + 1, \
                      cols | curr_col, \
                      (pies | curr_col) << 1, \
                      (nas | curr_col) >> 1 )

        dfs('', 0, 0, 0, 0)
        return [["."*(n-ord(C)+48-1) + "Q" + "."*(ord(C)-48) for C in sol] for sol in ans]

