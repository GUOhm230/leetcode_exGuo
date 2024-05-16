"""
300.最长递增子序列
# 其实做的时候排除了几个做法。关键是做的时候心不够镇定
该问题要搞清楚两点：
1. 整个序列的递增序列，一般都要用动态规划的思路。
2. 既然动态规划，那么就要有dp[i]或者dp[i][j]无论怎么样都要和新加入的nums[i]进行比较，也就是说nums[i]必然要在dp[i]表示的序列中，
所以其实我之前已经想到了以nums[i]作为结尾的最大递增序列，但是陷入一个误区，也就是非要nums[i]和nums[i-1]比较若结果为大于则dp[i]=dp[i-1]+1.
以为这样下去会导致得到的值为连续的。实则我是忘了一个点了，以该数字为结尾的最大严格递增子序列不一定为全场最大，且nums[i]>nums[i-1]就不代表dp[i]=
dp[i-1]+1.因为存在这样的数组[0, 2, 3, 1, 4, 5, 7]。dp[3]=2, 但是nums[3]>nums[3],而此时dp[2]=3,且4>2所以此时的最大递增子序列长度为4.
也就是说要和之前的每个nums[j]进行比较，如果nums[i]>nums[j]，此时的dp[i]=dp[j]+1
该方法的时间复杂度是O(n^2)， 空间复杂度是O(n)
"""
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 不太确定的dp解法
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                j = i - 1
                while j > 0:
                    print(i, j)
                    if nums[i] > nums[j]:
                        dp[i] = dp[j] + 1
                        break
                    else:
                        j -= 1
                if j == 0:
                    dp[i] = 1
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        # 这里是对的
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,4,7]
    result = s.lengthOfLIS2(nums)
    print(result)