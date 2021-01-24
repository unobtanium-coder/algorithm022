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
1������״̬
   dp[i,j]��ʾ�����Ͻ�(0,0)�����꣨i,j������С·����
  m = len(grid)
  n = len(grid[0])
  ���Ͻ�dp[0][0]
  ���½�dp[m][n]
2��״̬ת�ƣ������߽�������
  dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
  ���߽�������Ҫ��֤ i-1>=0, j-1>=0 �� i>0, j>0��
3����ʼ��
  dp[0][0] = grid[0][0]
4������˳��
  Ϊ��֤��2���еı߽�������
  Ӧ���ȵ�������dp[0][j]��dp[i][0]
  ����˫��ѭ���������ɣ��������б߽�����
  ע������
                  dp[i][j] = grid[i][j] + \
                            min( dp[i-1][j] if i>0 else float('inf'), \
                                 dp[i][j-1] if j>0 else float('inf')  )
   ����������list index out of range��
   ��Ϊ��ִ��if�Ӿ�ǰ�Ѿ���ִ����dp[i-1][j]
   �ʶ�ֻ�ܲ�ȡ���� ���������� �ٵ��� ��˳��
5�����
    dp[m-1][n-1]
"""
