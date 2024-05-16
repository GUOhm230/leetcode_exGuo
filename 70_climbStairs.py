"""
题目描述：爬楼梯
"""
class Solution:
    def climbStairs(self, n:int)->int:
        # 方法一：使用递归方法。但是时间复杂度和空间复杂度双高，尤其时间复杂度为O(2^n)。2^n次方就是深度为n的二叉树所有节点数
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def c2(self, n):
        # 方法二。递归的主要问题是从后往前推导，但是又需要从前往后计算。因此复杂度很高。那么我从前往后逐个计算呢？
        # 这样的时间复杂度应该是O(n)，同时用一个容器保存中间数据,这样空间
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1, 2]
        for i in range(3, n + 1):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]

    def c3(self, n):
        # 每次其实只要两个数据即可，因此可以把空间复杂度从O(n)变成O(1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1, 2]
        for i in range(3, n + 1):
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
        return dp[-1]

    def c4(self, n):



