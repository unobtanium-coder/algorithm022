class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        def isAlpha(ch):
            return "A" <= ch <= "Z" or "a" <= ch <= "z"

        n = len(S)
        i = 0
        j = n - 1
        ans = ""
        while j >= 0:
            while i < n and not isAlpha(S[i]):
                ans += S[i]
                i += 1

            while j >= 0 and not isAlpha(S[j]):
                j -= 1
            
            if j >= 0:
                ans += S[j]
                j -= 1
                i += 1
        
        while i < n:
            ans += S[i]
            i += 1
        
        return ans

