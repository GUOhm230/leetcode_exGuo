class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # 和上一题很相似啊，也和最长公共子序列相似，故解法其实类似。不能说类似，简直是一模一样
        n, m = len(s1), len(s2)
        result = 0
        if n == 0 or m == 0:
            for i in range(n + m):
                result += ord((s1 + s2)[i])
            return result
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = ord(s1[0]) + ord(s2[0]) if s1[0] != s2[0] else 0
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] - ord(s1[i]) if s1[i] == s2[0] and dp[i - 1][0] == sum(ord(k) for k in s1[:i])+ord(s2[0]) else \
            dp[i - 1][0] + ord(s1[i])
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] - ord(s2[j]) if s1[0] == s2[j] and dp[0][j - 1] == sum(ord(k) for k in s2[:j])+ord(s1[0]) else \
            dp[0][j - 1] + ord(s2[j])
        print(dp)
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j - 1] if s1[i] == s2[j] else min(dp[i - 1][j - 1] + ord(s1[i]) + ord(s2[j]),
                                                                       dp[i - 1][j] + ord(s1[i]),
                                                                       dp[i][j - 1] + ord(s2[j]))
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    s1 = "sea"
    s2 = "eat"
    # s1.pop("e")
    # result = s.minimumDeleteSum(s1, s2)
    # print("result=", result)
    # print(sum(ord(i) for i in s1))
    # b = min(len(s1), len(s2))
