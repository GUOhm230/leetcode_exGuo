"""
740. 删除并获得点数
"""
class Solution:
    def deleteAndEarn(self, nums) -> int:
        # 如果对这些元素排好序，然后提出其中的重复元素，那么就成了一个打家劫舍问题
        # 实际不是，因为并不是中间都可以跳过。因此问题并不在此
        # 但是一般含有重复元素，我需要重复元素剥离的时候，就要用到双指针。因此本阶段也同样可以
        # 做法肯定是对的，接下来还是要完善一下,转移方程清楚，关键是边界条件，也清楚，但是从哪开始双指针呢
        # 还是细节问题，关键问题是从一开始就重复怎么办，因此需要往后移动一位。这样的话，也不用单独将n==2提出来
        # 做法绝对没有问题，单身本身
        # nums = sorted(nums)
        # n = len(nums)
        # dp = [0] * (n+1)
        # dp[0] = 0
        # dp[1] = nums[0]
        # if n == 1:
        #     return nums[0]
        # if n >= 2:
        #     pre, curr = 0, 2
        #     pre_list = [0]
        #     # if nums[0] == nums[1]:
        #     #     curr = 2
        #     # else:
        #     #     pre=1
        #     #     curr=2
        #     #     pre_list.append(pre)
        #     while curr <  n+1:
        #         # 先计算循环至当前位置能获得的最大操作点数
        #         # 以相邻位置是否差1区分。
        #         if nums[curr-1] != nums[curr-2]+1:
        #             # 不相邻也要区分了，因为不相邻中存在相等且与之前不等的相差为1的情况，而这种情况难以区分的是pre作为开头的例子
        #             # 除去开头位置，重复元素与紧邻的不等元素相差1时,这样做好麻烦啊，那只有把相等元素开始位置都保存起来
        #             if nums[curr-1] == nums[curr-2]:
        #                 if pre > 0 and nums[curr-1] == nums[pre-1] + 1: #
        #                     dp[curr] = max(dp[pre], dp[pre_list[-2]] + nums[curr-1] * (curr-pre))
        #                 # else:
        #                 #     dp[curr] = dp[curr-1]
        #             else:
        #                 pre = curr-1
        #                 pre_list.append(pre)
        #                 dp[curr] = dp[curr-1] + nums[curr-1]
        #         else:
        #             dp[curr] = max(dp[pre], nums[curr-1] + dp[pre_list[-2]])
        #             pre += curr-1
        #             pre_list.append(pre)
        #         curr += 1
        return dp[-1]

    def deleteAndEarn2(self, nums) -> int:
        # 转换成打家劫舍问题，真是太巧妙了。
        # 这道题与大家劫舍得区别在哪呢？其实关键还是问题的分析。因为一旦选择了相同的元素，无论该元素有多少个，都应该选择完该元素。但是之前认为不是打家劫舍的例子时认为这个中间位置是无法继续统一的
        max_num = max(nums)
        sum_val = [0] * (max_num+1)
        for val in nums:
            sum_val[val] += val
        def rob(sums):
            n = len(sums)
            first = sums[0]
            n = len(sums)
            if n==1:
                return sums[0]
            second = max(sums[0], sums[1])
            for i in range(2, n):
                first, second = second, max(sums[i] + first, second)
            return second
        return rob(sum_val)

if __name__ == "__main__":
    nums = [2, 2]
    s = Solution()
    results = s.deleteAndEarn(nums)
    print(results)