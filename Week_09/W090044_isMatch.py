class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:  return not s
        first_match = bool(s) and (p[0] in {s[0], '?'})
        if p[0] == '*':
            return self.isMatch(s, p[1:]) or \
                    bool(s) and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        """
        ע�� leetcode���� 1601 / 1811 ��ͨ���������� ��ʱ�� ���Ľ�
            ��ʱ������

"ababaaabbaabbabbababbaabbaababbaaabaabbaabbbbaabbaabab"
"*b**a"

        """

