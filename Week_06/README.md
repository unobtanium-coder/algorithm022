ѧϰ�ʼ�

DP�岽�裺

1������״̬

2��״̬ת�Ʒ��̣����߽�������

3����ʼ��

4������˳��ע������±�Խ�磩

5�����

-------------

�� leetcode#63 ����ͬ·��2�� Ϊ����

1������״̬

    dp[i][j] = �����Ͻ�(0,0)��(i,j)��·������

2��״̬ת�Ʒ��̣����߽�������

    if obstacleGrid[i][j] == 1:

        dp[i][j] = 0
    
    else:

        dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    (�߽�������������i-1/j-1>=0)

3����ʼ��

    m = len(obstacleGrid)

    n = len(obstacleGrid[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

4������˳��ע������±�Խ�磩

    for i in range(1, m):

        dp[i][0] = 0 if obstacleGrid[i][0] == 1 else min(1, dp[i-1][0])
    
    for j in range(1, n):
    
        dp[0][j] = 0 if obstacleGrid[0][j] == 1 else min(1, dp[0][j-1])
    
    for i in range(1, m):

        for j in range(1, n):
    
            ״̬ת�Ʒ��̣�������˳������Ȼ����߽����� i-1/j-1 >= 0��
5�����

    dp[m-1][n-1]


