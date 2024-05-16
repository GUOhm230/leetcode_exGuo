"""
1143.最长公共子序列
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cur_text2 = 0
        n = len(text1)
        m = len(text2)
        dp = [0]*n
        k=0
        while k < m:
            if text1[0] == text2[k]:
                cur_text2 = k
                dp[0]=1
                break
            k+=1
        if k==m:
            dp[0] = 0
        print(dp, cur_text2) # 一维肯定行不通
        for i in range(1, n):
            j=cur_text2
            while j<m:
                print(text1[i], text2[j], i, j)
                if text1[i] == text2[j]:
                    dp[i] = dp[i-1] + 1
                    cur_text2 = j
                    break
                j+=1
            if j==m:
                dp[i] = dp[i-1]
        return dp[-1]
    def longestCommonSubsequence2(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0] * n for _ in range(n)]  # dp[i][j]表示以i为开头的最长公共子序列数
        for i in range(n):
            cur_text2 = -1
            for j in range(i, n):

                k = cur_text2+1
                if j != i and dp[i][j - 1] == 0:  # 表明以他为开头的字符串没有公共子序列，之后也不必进行计算
                    print("直接退出：", i, j, dp[i][j-1])
                    break
                while k < m:
                    print("i, j=", i, j, k, text1[i:j + 1], text2[k])
                    if text1[j] == text2[k]:
                        dp[i][j] = dp[i][j - 1] + 1
                        cur_text2 = k
                        print("相等时：", i, j, k, text1[j], text2[k], dp[i][j])
                        break
                    k += 1
                # if k == m:
                #     break

        return max(max(dp[i]) for i in range(n))
    # 以上两种方法均行不通。其实我已经想到了相应的dp表达思路了。
    # 1. 为什么要用dp.2.dp二维矩阵如何表示
    # 这个才是最终答案。 其实是可以优化的
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0 if text1[0] != text2[0] else 1
        for j in range(n):
            if dp[0][j - 1] == 1 or text2[0] == text1[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        for i in range(m):
            if dp[i - 1][0] == 1 or text1[0] == text2[i]:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
        if n == 1 or m == 1:
            return max(dp[0][n - 1], dp[m - 1][0])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j - 1] + 1 if text2[i] == text1[j] else max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    text1 = "abcde"
    text2 = "ace"
    result = s.longestCommonSubsequence2(text1, text2)
    print(result)