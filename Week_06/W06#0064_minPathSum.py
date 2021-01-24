class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m==0 or n==0: return 0

        dp = [[0 for _ in range(n)]  for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1,m): dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n): dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]

        """
1、定义状态
   dp[i,j]表示从左上角(0,0)到坐标（i,j）的最小路径和
  m = len(grid)
  n = len(grid[0])
  左上角dp[0][0]
  右下角dp[m][n]
2、状态转移（描述边界条件）
  dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
  （边界条件：要保证 i-1>=0, j-1>=0 即 i>0, j>0）
3、初始化
  dp[0][0] = grid[0][0]
4、计算顺序
  为保证第2点中的边界条件，
  应首先单独计算dp[0][j]及dp[i][0]
  后续双重循环迭代即可，无须再判边界条件
  注：形如
                  dp[i][j] = grid[i][j] + \
                            min( dp[i-1][j] if i>0 else float('inf'), \
                                 dp[i][j-1] if j>0 else float('inf')  )
   这样的语句会list index out of range，
   因为在执行if子句前已经先执行了dp[i-1][j]
   故而只能采取上述 先首行首列 再迭代 的顺序
5、结果
    dp[m-1][n-1]
"""
