"""
最长严格递增子序列的个数
"""
from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        # convert = [[0]] # 记录当前元素要达到以该元素为结尾时的转移元素位置，第一个元素肯定是从0开始且有可能是多个。现在不管耗时
        max_count = [0] * n  # 为什么要记录转移呢？直接记录最大序列数不就好了，接下来只要从这转移，就能知道其中的最大个数了
        max_count[0] = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:  # 只有经过了这步，才表明dp[i]至少等于2
                    if dp[j] + 1 == dp[i]:
                        max_count[i] += max_count[j]
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        max_count[i] = max_count[j]

            if dp[i]==1:
                max_count[i]=1
        print("dp=", dp)
        print("max_count=", max_count)

        return 0

if __name__ == "__main__":
    s = Solution()
    # nums = [1,2,4,3,5,4,7,2]
    # nums = [1, 3, 5, 4, 7]
    # nums = [3, 1, 2]
    # result = s.findNumberOfLIS(nums)
    # print(result)
    l = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
    # ll = l.sort(key=lambda x:x[1])
    l.sort()
    # print(l)
    # for i in range(1, 0, -1):
    #     print(i)
    l = [1, 2, 3, 4]
    l[::] = [2] * 4
    print(l)