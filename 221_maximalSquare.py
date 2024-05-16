from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = matrix.copy()
        dp = dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) +1
                else:
                    dp[i][j] = 0
        print(dp)
        print(dp[3])
        for i in range(m):
            print("test:", dp[i])
        print(max(dp[i] for i in range(m)))
        return max(max(dp[i]) for i in range(m)) ** 2

if __name__ == "__main__":
    s = Solution()
    # matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    # result = s.maximalSquare(matrix)
    # print(result)
    for i in range(5, 0, -1):
        print(i)
    # s = "guohuiming"
    # print(s[2:3])