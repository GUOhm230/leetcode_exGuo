"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
"""
class Solution:
    def minPathSum(self, grid) -> int:
        # 和上一题不同路径其实是如出一辙的。dp[i][j] = min(dp[i-1][j] + dp[i][j-1])
        # 关键是初始条件
        m = len(grid)
        n = len(grid[0])
        dp = grid # 为什么这样就没有问题。而创建一个新的全0二维列表就会出错呢?这个问题后面还是需要思考的
        for i in range(1, n):
            dp[0][i] += dp[0][i-1]
        print(dp[0])
        for j in range(1, m):
            dp[j][0] += dp[j-1][0]
            print(dp[j][0])
        print("dp[1][1]=", dp[1][1])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    # grid = [[1, 2], [1, 1]]
    grid = [[7, 4, 8, 7, 9, 3, 7, 5, 0], [1, 8, 2, 2, 7, 1, 4, 5, 7], [4, 6, 4, 7, 7, 4, 8, 2, 1], [1, 9, 6, 9, 8, 2, 9, 7, 2],
     [5, 5, 7, 5, 8, 7, 9, 1, 4], [0, 7, 9, 9, 1, 5, 3, 9, 4]]
    result = s.minPathSum(grid)
    print(result)