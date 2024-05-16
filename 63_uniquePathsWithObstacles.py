from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        # 这道题和之前的题仿佛没有什么区别，无非就是多了一次判定
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = obstacleGrid
        flag = 0
        if dp[0][0] == 1:
            dp[0][0] = 0
            flag = 1
        else:
            dp[0][0] = 1
        print(dp[0][0])
        for i in range(1, n):
            if flag == 0 and obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
                flag=1
        flag = 0
        for j in range(1, m):
            if dp[0][0] == 1 and flag == 0 and obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                dp[j][0] = 0
                flag=1
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        # 这道题和之前的题仿佛没有什么区别，无非就是多了一次判定
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = obstacleGrid
        flag = 0
        dp[0][0] = 0 if dp[0][0] == 1 else 1
        for i in range(1, n):
            if flag == 0 and dp[0][0] == 1 and obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
                flag = 1
        flag = 0
        for j in range(1, m):
            if dp[0][0] == 1 and flag == 0 and obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                dp[j][0] = 0
                flag = 1
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def s3(self, l):
        # 这个优化通过了。
        m = len(l)
        n = len(l[0])
        dp = [[0]*n]*m
        print(id(l), id(dp))
        dp[0][0] = 0 if l[0][0] == 1 else 1
        print(dp)
        print(l)
        for i in range(m):
            for j in range(n):
                if l[i][j] == 1:
                    dp[i][j] = 0
                elif i > 0 and j > 0:
                    print(dp[i - 1][j], dp[i][j-1])
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j]
                print("i={}, j={}, dp={}".format(i, j, dp[i][j]))
        return dp[-1][-1]

    def s4(self, obstacleGrid):
        # 用滚动数组优化一下
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [0] * n  # 按行进行
        f[0] = 0 if obstacleGrid[0][0] == 1 else 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                elif j > 0:
                    f[j] += f[j - 1]
        return f[-1]

if __name__ == "__main__":
    s = Solution()
    l = [[0,0],[1,1],[0,0]]
    # result = s.uniquePathsWithObstacles(l)
    # print(result)
    # dp = [0 if l[0][0] == 1 else 1]
    # print(dp)
    l2 = [[0,0,0],[0,1,0],[0,0,0]]
    # result2 = s.uniquePathsWithObstacles2(l2)
    result3 = s.s3(l2)
    print(result3)
