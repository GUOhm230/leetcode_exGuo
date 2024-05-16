"""
1027.最长等差数列
"""
from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # 这道题和最长递增子序列应该没有什么差别吧.不对啊，这个
        """
        这里的思路出现了问题，和递增是不一样的。因为当前nums[i]如果大于nums[j]则以i为结尾且从j转换的最长严格递增子序列必然只有这一个。不存在当前从j转移的最长严格递增子序列现在要小，
        但是之后会更大的情况。
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [2] * n
        dp[0] = 1
        difList = [[None]*n for _ in range(n)]
        difList[1][0] = nums[1] - nums[0]
        # 三层循环有点晕了。
        for i in range(1, n):
            print("-------------------i={}, nums[i]={}------------------------".format(i, nums[i]))
            max_temp = dp[i]
            # 第二层循环用于当前nums[i]与每个nums[j]进行比较。其与这些元素进行比较，但是比较的时候我又不知道他们的差值是多少，从哪转移过来的
            # 假如有多个相同的长度，就需要逐一进行运算,找到相等差值相等者，有相等的话，就加一
            # 所以本处还要更新一下：也就是如果所有数字相等呢？所以不等于0这一项是不靠谱的
            for j in range(i):
                for k in range(j):
                    if difList[j][k] != None and nums[i]-nums[j] == difList[j][k]:
                        print("j={}, k={}, nums[i]={}, nums[j]={}, nums[i]-nums[j]={}, difList[j][k]={}, dp[j]={}".format(j, k, nums[i], nums[j], nums[i] - nums[j], difList[j][k], dp[j]))
                        if dp[j] + 1 == max_temp:
                            difList[i][j] = nums[i] - nums[j]
                        if dp[j]+1 > max_temp:
                            difList[i][::] = [None] * n
                            dp[i] = dp[j] + 1
                            max_temp = dp[i]
                            difList[i][j] = nums[i] - nums[j] # 这里更新了，但是其他数字要退回啊

                if dp[i] == i+1:
                    # print("这里退出吗：", dp[i])
                    break
                if dp[i] == 2:
                    difList[i][:i] = [nums[i]- nums[j] for j in range(i)]
            print(dp[i], difList[i][::])
        return max(dp)

    def longestArithSeqLength2(self, nums: List[int]):

        minv, maxv = min(nums), max(nums)
        diff = maxv - minv
        ans = 1

        for d in range(-diff, diff + 1):
            f = dict()
            print("---------------------------------------------")
            for num in nums:
                if (prev := num - d) in f:
                    f[num] = max(f.get(num, 0), f[prev] + 1)
                    ans = max(ans, f[num])
                    print("d={}, ans={}, num={}".format(d, ans, num))
                    # if ans==6:
                    #     print("6:", num)
                    # if ans == 5:
                    #     print("5:",num)

                f[num] = max(f.get(num, 0), 1)
            print(f)
        #
        return ans


if  __name__ == "__main__":
    # nums = [3,6,9,12]
    # nums = [20,1,15,3,10,5,8]
    # nums = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
    nums = [44,46,22,68,45,66,43,9,37,30,
            50,67,32,47,44,11,15,4,11,6,
            20,64,54,54,61,63,23,43,3,12,
            51,61,16,57,14,12,55,17,18,25,
            19,28,45,56,29,39,52,8,1,21,
            17,21,23,70,51,61,21,52,25,28]
    # nums = [-2] * 999
    # nums[35] = 4
    # nums[782] = 10
    # nums.sort()
    # print(nums)
    # print(len(nums))
    # s = Solution()
    # result = s.longestArithSeqLength(nums)
    # print("result=", result) # [15, 17, 19, 21, 23, 25]
    # l = [2, None, 3, None]
    # print(len(l))
    # l = [[None]*2 for _ in range(3)]
    # l[1][0] = 1
    # print(l)
    # 海象运算符学习一下
    my_list = [1, 2, 3, 4]
    # if (count=len(my_list)) > 3:
    #     print("测试通过")

    if (count := len(my_list)) > 3:
        print("海象运算符测试通过")