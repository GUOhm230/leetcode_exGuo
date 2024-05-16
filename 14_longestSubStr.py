"""
题目：最长公共前缀问题
输入一个字符串数组，输出公共子串
算法思想：
1. 找到第一个和第二个的公共子串部分。然后和第三个，第四个用同样的方法进行
2. 好了，关键问题是怎么找到第一个和第二个的公共子串部分
3. 逐个比较
4. 好像这样行不通，如果当前比较发现最长子串不止一个呢？那接下来不是很麻烦嘛？
5. 题目看错了。答案是最长公共前缀，而非最长公共子串。所以思路是行得通的。10分钟就完成了
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """我自己写的代码"""
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        start = strs[0]
        print()
        for i in range(1, len(strs)):
            length = min(len(start), len(strs[i]))
            # 需要考虑到最小长度为0的情况，此时不会进入循环
            if length == 0:
                return ""
            for j in range(length):
                print("这个j", j)
                print(start[j], strs[i][j])
                # 如果两个不等，则更新start到等为止。但是，如果前length个字符串均相等，那应该怎么办呢？
                if start[j] != strs[i][j]:
                    start = start[:j]
                    break
                if j==length-1:
                    start = start[:length]
        return start

    def s2(self, strs):
        """
        官方提供的，横向法，这部分的代码写的需要多学习一下
        学到的东西：
        1. 封装，有个独立的功能便可以封装
        2. 本处有一个情况需要考虑，也就是如果只有一个字符串的情况，那就需要返回第一个字符串的。本处的处理比较巧妙，
        而我则多建了一个保存字符串的变量，而且多了一次字符串的判定。这样增加了时间复杂度和空间复杂度
        3. while的使用，相对比较灵活，而我则一直在用for，却相对来说比较死板。而且这个index的用法也是可圈可点。
        好处是每次比较只需要比较当前那个，而不是比较之前的所有字符串
        所以现在去改进下我之前的代码
        4. 没啥改进的。如果不是用while则不太好改进，只是把连续长串改成了单独的串
        改进成功了，但是总是忽略某些特殊情况。改进之后时间减半几乎
        """
        if not strs:
            return ""
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            # 这个代码需要好好学一下
            if not prefix:
                break
        return prefix

    # 获得两个字符串的最长公共前缀
    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

    def s3(self, strs):
        """
        本段为主要内容：也就是分治法的使用
        算法思想：把字符串数组分成两边，每边再进行分治
        主要在于思想，其实时空调复杂度是一样的，且由于递归调用要维持递归栈，反而耗时更长
        """
        # 两个输入为当前字符串数组的初始索引和最终索引
        # 输出就是当前的字符串数组的最长公共前缀
        def lcp1(start, end):
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp1(start, mid), lcp1(mid+1, end) # 返回的是这两个字符串数组的最长公共子串
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                # 最后只剩两个字符串数组，因此，如果两个字符串数组只要不等，就返回当前字符串所在位置即可啊
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            # 前minlength均相等，或者干脆不进入for循环，也就是说minlength=0的情况下，则返回如下值
            return lcpLeft[:minLength]
        return "" if not strs else lcp1(0, len(strs)-1)




if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    S = Solution()
    results = S.longestCommonPrefix(strs)
    print("最终结果：", results)
    # sss = "abc"
    # print(max("abc"))
    # print(min("abc"))
    a = [1, 2, 3, 4]
    b = [1, 2]
    i = 0
    while a and b:
        print(a[i], b[i])
        i += 1

