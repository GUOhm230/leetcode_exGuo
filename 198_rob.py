"""
动态规划经典
题目描述：
打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
题目分析：
官方解释确实相对简单一些。而我是借用了最小花费爬楼梯的思路：
要求的是偷完n间房后的最大收入，也就是进入第i间房时的最大收入，而进入第i间房有两种方式：
1）从i-1进入或者从i-2进入
2）从i-1进入则偷盗数额为nums[i-1] + dp[i-2]也就是进入第i-2房时的偷窃数额
3）从i-2进入则为nums[i-2]+dp[i-3]
4) 由于有i-3这个，因此，循环必须从i=3开始，所以i=1, 2时需要另算
5）边界条件比较清楚：第0间房时dp=0, 第一间房时dp=nums[0]， 第二间房时dp=max(nums[0], nums[1])

看过答案解析之后认为可以进行优化
1. 以进入i房间为目标和以偷完i个房间为目标获得的最大收入是一个意思
2. 按照我之前的分法同样是按照偷盗i号房以及不偷盗i号房为分类
3. 偷盗i号房的偷盗金额为nums[i] + dp[i-2].
4. 不偷盗i号房的偷盗金额就是dp[i-1]
5. 这样的话，边界条件也需要修改一下。dp[0]=nums[0], dp[1]=max(nums[0], nums[1])
6. 实际上，这样做的时空复杂度基本是不变的都是O(n)。意义就在于代码可以简单一些
"""

class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        else:
            dp[2] = max(nums[0], nums[1])
            for i in range(3, n+1):
                dp[i] = max(nums[i-1] + dp[i-2], nums[i-2] + dp[i-3])
        return dp[-1]

    # 优化后，时空复杂度其实依然不变
    def rob2(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n==1:
            return nums[0]

        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

    # 再优化下：滚动数组模式，也就是只用2个存储，时间复杂度到O(2)
    def rob3(self, nums):
        first = nums[0]
        n = len(nums)
        if n == 1:
            return nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, n):
            # 这里其实作为数据的交换是可以的
            first, second = second, max(nums[i] + first, second)
        return second