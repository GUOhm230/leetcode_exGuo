"""
718. 最长重复子数组
"""
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        text1 = ""
        text2 = ""
        n = len(nums1)
        m = len(nums2)
        for i in nums1:
            text1+=str(i)
        for j in nums2:
            text2+=str(j)
        print("转字符串：", text1, text2)
        max_len = 0
        for i in range(n):
            for j in range(i, n):
                print(i,j, j-i+1, text1[i:j+1])
                if text1[i:j+1] in text2 and j-i+1 > max_len:
                    print("最大值：", max_len)
                    max_len=j-i+1
        return max_len

if __name__ == "__main__":
    s = Solution()
    nums1 = [0,1,1,1,1]
    nums2 = [1,0,1,0,1]
    result = s.findLength(nums1, nums2)
    print(result)
