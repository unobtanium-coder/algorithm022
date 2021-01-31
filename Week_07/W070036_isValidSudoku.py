class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def judge(grid: str, ss: set) -> bool:
            # print(grid, ss)
            if grid==".": return True
            if grid in ss: return False
            ss.add(grid)
            return True

        for i in range(9):
            set_c = set()
            set_r = set()
            set_b = set()
            for j in range(9):
                # print("3sets befor ij:",set_c, set_r, set_b)
                if not judge(board[i][j], set_c): 
                    print(i,j,"i,j,False!")
                    return False
                # print("3sets befor ji:",set_c, set_r, set_b)
                if not judge(board[j][i], set_r): 
                    print(i,j,"j,i,False!")
                    return False
                # print("3sets befor bl:",set_c, set_r, set_b)
                block_ul_x = 3 * (i % 3)
                block_ul_y = 3 * (i // 3)
                grid_x = block_ul_x + (j % 3)
                grid_y = block_ul_y + (j // 3)
                if not judge(board[grid_x][grid_y], set_b): 
                    # print(i,j,block_ul_x,block_ul_y,grid_x,grid_y,"block False!")
                    return False
        return True
    

