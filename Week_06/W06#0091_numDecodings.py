class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n==0: return 0
        if s[0]=='0': return 0

        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            if s[i-1]=='0':               #XXXXXXXXX0
                if s[i-2] in {'1','2'}:           #XXXX[1-2]0
                    dp[i] = dp[i-2]
                else:                         #XXXX[3-9,0]0
                    return 0
            elif s[i-1]<='6':               #XXXXXXXXX[1-6]
                if s[i-2] in {'1','2'}:           #XXXX[1-2][1-6]
                    dp[i] = dp[i-2] + dp[i-1]
                else:                         #XXXX[3-9,0][1-6]
                    dp[i] = dp[i-1]
            else:                         #XXXXXXXXX[7-9]
                if s[i-2] == '1':               #XXXX[1][7-9]
                    dp[i] = dp[i-2] + dp[i-1]
                else:                         #XXXX[0,2-9][7-9]
                    dp[i] = dp[i-1]
            print(s[:i],dp)

        print(dp)
        return dp[n]

        """
1������״̬
  dp[i]Ϊs[0:i]�ģ���0..(i-1)�������еĽ�������
  ���У�dp[0]�ض�Ϊ1
2��״̬ת�ƣ������߽�������
  ����dp[i]ʱ��
    if s[i-1]=='0':               #XXXXXXXXX0
        if s[i-2] in {'1','2'}:           #XXXX[1-2]0
            dp[i] = dp[i-2]
        else:                         #XXXX[3-9,0]0
            return 0
    elif s[i-1]<='6':               #XXXXXXXXX[1-6]
        if s[i-2] in {'1','2'}:           #XXXX[1-2][1-6]
            dp[i] = dp[i-2] + dp[i-1]
        else:                         #XXXX[3-9,0][1-6]
            dp[i] = dp[i-1]
    else:                         #XXXXXXXXX[7-9]
        if s[i-2] == '1':               #XXXX[1][7-9]
            dp[i] = dp[i-2] + dp[i-1]
        else:                         #XXXX[0,2-9][7-9]
            dp[i] = dp[i-1]
    
    �����ڳ�ʼ��ʱ����dp[0],dp[1]��i��2���𣬱߽������϶����㣬��������ж���

  ע������ʾ��3��������������ֱ�ӷ��� 0
       ��s[0]=='0' ��ֱ����� 0
       ���м����'0'��������ǰ���ֽ��ʱ��ֻ����'10'/'20'���������ֱ����� 0
3����ʼ��
  ���� if s[0]=='0': return 0
  dp[0], dp[1] = 1, 1
4������˳�򼰷�Χ
  i in range(2,n+1)
5�����
  dp[n]
"""
