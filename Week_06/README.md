
DP五步骤：

1、定义状态

2、状态转移方程（含边界条件）

3、初始化

4、计算顺序（注意避免下标越界）

5、结果




以 leetcode#63 “不同路径2” 为例：

1、定义状态

dp[i][j] = 从左上角(0,0)到(i,j)的路径条数

2、状态转移方程）( 含边界条件 )

if obstacleGrid[i][j] == 1:

    dp[i][j] = 0

else:

    dp[i][j] = dp[i][j-1] + dp[i-1][j]

(边界条件：需满足i-1/j-1>=0)

3、初始化

m = len(obstacleGrid)

n = len(obstacleGrid[0])

dp = [[0 for _ in range(n)] for _ in range(m)]

dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

4、计算顺序（注意避免下标越界）

for i in range(1, m):

    dp[i][0] = 0 if obstacleGrid[i][0] == 1 else min(1, dp[i-1][0])

for j in range(1, n):

    dp[0][j] = 0 if obstacleGrid[0][j] == 1 else min(1, dp[0][j-1])

for i in range(1, m):

    for j in range(1, n):

        状态转移方程（按以上顺序，已自然满足边界条件 i-1/j-1 >= 0）

5、结果

dp[m-1][n-1]


