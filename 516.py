class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 和前面的回文子串是一样的
        n = len(s)
        dp = [[1]*n for _ in range(n)]
        for i in range(n-1):
            dp[i][i+1] = 2 if s[i]==s[i+1] else 1
        for L in range(3, n+1):
            for i in range(n-L+1):
                j = i+L-1
                dp[i][j] = dp[i+1][j-1] + 2 if s[i]==s[j] else dp[i+1][j-1]
        print(dp)
        return max(max(dp[i]) for i in range(n))

if __name__ == "__main__":
    st = "bbbab"
    # s = Solution()
    # result = s.longestPalindromeSubseq(st)
    # print(result)
    n = len(st)
    str = [[""] * n for _ in range(n)]
    for i in range(n):
        str[i][::] = st[i]*n
    print(str)

