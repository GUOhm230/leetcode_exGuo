"""
72. 编辑距离
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 这道题目其实就是最长公共子序列的变体
        n, m = len(word1), len(word2)
        dp=[[0]*m for _ in range(n)]
        dp[0][0] = 0 if word1[0]==word2[0] else 1
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] if word1[i]==word2[0] and dp[i-1][0]==i else dp[i-1][0]+1
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] if word1[0]==word2[j] and dp[0][j-1]==j else dp[0][j-1]+1
        print(dp)
        for i in range(1, n):
            for j in range(1, m):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        return dp[-1][-1]

if __name__ == "__main__":
    # s = Solution()
    # word1 = "mart"
    # word2 = "karma"
    # result = s.minDistance(word1, word2)
    print(ord("a"))
