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
1、定义状态
  dp[i]为s[0:i]的，即0..(i-1)数字序列的解码总数
  其中，dp[0]特定为1
2、状态转移（描述边界条件）
  计算dp[i]时，
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
    
    （由于初始化时特设dp[0],dp[1]且i从2算起，边界条件肯定满足，无需额外判定）

  注1：根据示例3，以下两种特判直接返回 0
       a)s[0]=='0' 则直接输出 0
       b)中间出现'0'而必须与前数字结合时，只能是'10'/'20'，其他情况直接输出 0
  注2：本题为使满足边界条件，使dp[i]与s[i-1]错了一位来对应，如下示意：
           X  X    A         B         C         D      X  X  X
     s[?]    ..   ...     s[i-3]    s[i-2]    s[i-1]  ...
     dp[?]  ... dp[i-3]  dp[i-2]   dp[i-1]    dp[i]   ...
        带来的另一影响是：dp数组共需n+1个元素[0..n]
3、初始化
  特判 if s[0]=='0': return 0
  dp[0], dp[1] = 1, 1
4、计算顺序及范围
  i in range(2,n+1)
5、结果
  dp[n]
"""
