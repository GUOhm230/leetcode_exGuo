"""
35_搜索插入位置
分治法的使用
"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # 分治法O(logn).思路是没有错滴，那问题还是在边界条件的判定上
        n = len(nums)
        if n == 1:
            if nums[0] >= target:
                return 0
            else:
                return 1
        low = 0
        high = n - 1
        while low != high:
            if high - low == 1:
                if target > nums[low] and target < nums[high]:
                    return low + 1
                elif target <= nums[low]:
                    return low
                elif target == nums[high]:
                    return high
                else:
                    return high + 1
            mean = (low + high) // 2
            if nums[mean] == target:
                return mean
            elif nums[mean] > target:
                high = mean
            else:
                low = mean

    def searchInsert2(self, nums, target):
        # 上面算法还是同样的问题。思路是对的。但是总是边界条件处理的不好。考虑的情况较少。做以下改进：
        # 1. 之后更新mid不用直接等于mid而是可以是mid的后一位或者前一位
        # 2. 更新循环条件。之前的更新是l与r不等的情况。但是实际上，l与r有可能会大于或者小于他们
        """
        还是要分析一下这个代码为什么要这么做。这样写就比我自己写的简洁多了
        问题一：为什么l以及r未来的变换需要跳过这个mid，无论是从左跳过还是从右跳过？
        答：很显然，因为nums[mid]已经和target比较过了，再比较一次就没有什么必要了。
        且后续的比较会在重复的比较中失去时间。而且无法掌控边界条件。

        问题二：为什么能以l<=r作为循环的条件？
        答：因为按照正常数据来说，l一般都是小于r的。当两个指针指向差1（r-l=1）的时候说明还有2个元素没有经过比较。此时mid=l,经过下一轮比较，其实也就是target
        和nums[l]进行比较，每次比较不外乎两种结果：等于，则返回该值。如果不等于，则要么l=mid+1=r,或者r=mid-1=l。也就是说，此时必定只剩一个元素了。再之后的比较
        l,r的变换就要错位了。
        因此也就是说，用分治法在判断的时候，最后一定会比较到只剩一个元素的情况。这个时候mid=l=r.如果等于自然return.如果target大于，则l=mid+1.此时要插入的位置仍然是l位
        如果小于，则h=mid-1.此时插入的位置应该是替代了先前的l位。。之后则无需进行比较累

        问题三：为什么返回的是l，而不是其他的呢？
        答：因为每次mid的计算是向下取整。且如果没有相等的元素，则每次必然比较到最后一个元素。最后的比较中如果target更大，则l应该左移一位，且数值应当在当前数值的右边。如果target更小
        则该数值应该取代l原本的位置。

        故而，做这类题目的时候，还是应该先分析其边界条件，不然容易出现判断失误的情况。而这个边界条件
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid+1
            else:
                l = mid-1
        return l





if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    result = s.searchInsert(nums, target)
    print(result)
