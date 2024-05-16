from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 其实做法和之前的并无二致，关键问题是需要记录这个最小值。这里不通过，因为并不是上个最小加上当前行就是最小了。存在当前行中出现一个比较小的值。
        flag = 0
        n = len(triangle)
        if n==1:
            return triangle[0][0]
        dp = [0]*n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            print(triangle[i][flag], triangle[i][flag+1])
            if triangle[i][flag] > triangle[i][flag+1]:
                dp[i] = dp[i-1] + triangle[i][flag+1]
                flag += 1
            else:
                dp[i] = dp[i-1] + triangle[i][flag]
            print(dp[i])
        return dp[-1]

    def s2(self, triangle):
        # 基于上面的错误，本次改正应该是没有问题了
        dp = triangle.copy()
        n = len(triangle)
        print(dp[0][0])
        if n == 1:
            return triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                # 还要改进，
                if j > 0 and j < i:
                    print(i, j)
                    print()
                    dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j])
                elif j==0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += dp[i-1][j-1]
        return min(dp[n - 1])

    def s3(self, triangle):
        # 以上算法还能继续优化
        # 优化点：1. j=0部分以及i=j部分可以不进行判定，直接求解。这样就优化了代码，并且可以减少判定时间
        dp = triangle.copy()
        p = triangle.copy()
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        for i in range(1, n):
            dp[i][0] += dp[i-1][0]
            for j in range(1, i):
                # 还要改进，
                dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j])
            dp[i][i] += dp[i - 1][i - 1]
        return min(dp[n - 1])

    def s4(self, triangle):
        # 优化点 2. 空间优化。每次计算的时候，都只用到了上一层的两个数值。但是按照之前的做法，好像是无法优化的。
        pass

if __name__ == "__main__":
    s = Solution()
    # t = [[2],[3,4],[6,5,7],[4,1,8,3]]
    t = [[-1],[2,3],[1,-1,-3]]
    # result = s.minimumTotal(t)
    # result = s.s2(t)
    # print(result)
    # print([[0] * 5 for _ in range(2)])

    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    m = len(matrix)
    n = len(matrix[0])
    dp = matrix.copy()
    for i in range(m):
        for j in range(n):
            dp[i][j] = int(matrix[i][j])
    dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
    print(max(max(dp)))

