"""
28: 主串以及模式串的匹配问题：数据结构算法中的关键问题。字符串匹配

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 特殊情况暂时不管，后面补充.准备暴力解法
        # 解决之后发现
        # 结果应该是对了，但是超出时间限制了
        n = len(haystack)
        m = len(needle)
        first, second = 0, 0
        head = 0 #如果在相等的时候找到了第二次和1相等
        pre_head = -1 # 记录上一个使用head的情况，这样防止重复并陷入死循环
        flag = 0
        while second < n:
            # print(haystack[second], first, second)
            if haystack[second] == needle[second - first]:
                # 等于中间某个值得时候，同样会可能等于该字符串的开头
                if haystack[second] == needle[0] and flag==0 and second != first:#and flag==0 and second != first: # 等于一次应该不能再更新了
                    head = second # 这样的话，每次不等之后，都从head开始，这样的话，实在耗时太长。更新一下
                    flag = 1
                if second - first + 1 == m:
                    return first
                second += 1
                print("first, second, head=", first, second, head)
            else:
                # 也就是当前轮的判定已经结束，需要开始新一轮的判定，而这个新一轮的判定不应该从下一个字符开始，因为极有可能在存在前后两段重复的字符。
                # 而这个新一轮的判定却有多种情况：
                # 1. 已经遍历的h列表中有到目前为止的片段依然满足当前片段的前几个。此时需要从head开始新一轮的遍历，其中可能存在回溯
                # 2. 当前遍历的字符与n字符串中第一个字符相同，而上一个开始字符又预制重复

                # 不相等的情况下,还有一种没有考虑到
                if head != 0 and (n-head) >= m and head != pre_head:
                    first = head
                    second = head
                    pre_head = head
                    flag = 0
                else:
                    if haystack[second] == needle[0]:
                        print(haystack[second], needle[0])
                        first = second
                        second += 1
                    else:
                        second += 1
                        first = second
            # if second - first + 1 == m:
            #     return first
            # print(haystack[second], first, second)
        return -1
    def strStr2(self, s1, s2):
        # 上面的代码过于复杂，我是单个进行判定，然后逐个进行判断，而实际上可以一按照滑动窗进行匹配则快很多
        n = len(s1)
        m = len(s2)
        for i in range(n):
            if n-i+1 < m:
                return -1
            print(s1[i:(i+m)])
            if s1[i:(i+m)] == s2:
                return i
        return -1

    # 按照简单字符串的匹配算法进行
    # 算法思想：从头开始遍历主串和模式串。当字符对齐时就同时向右移动并比较。如果有一位不对齐，则返回至主串与模式串本轮比较的开始位置处，向后一位重复操作。
    def strStr3(self, S1, S2):
        # 一遍AC通过。这样做就很清楚了。这个做法其实和strStr2是一样的，只是一个是一次性比较整个字符串
        n = len(S1)
        m = len(S2)
        i, j = 0, 0
        while i<n and j < m:
            if S1[i] == S2[j]:
                if j==m-1:
                    return i-j
                i += 1
                j += 1
            else:
                i = i-j+1
                j = 0
        return -1

    # 上面的都是一个思路，一直都要回溯，没有用到当前比较了多少个元素。而这个值只与模式串也就是子串有关。于是引出来KMP算法。
    # 该算法的主要改进点就是每当匹配失败的时候， 不对指针i进行回溯，再对j=0的子串进行一次重新匹配。kmp算法此时对i保持不变，而j也不再只等于0。因为他可能前面有几个是已经匹配好的字符串。而当匹配失
    # 败时j的取值，才是本次算法的关键问题。也是最难的一环。而这个，我在自己做算法的时候也实现了。
    # 看了两天了，终于搞懂了，真不容易啊
    def strStr4(self, S1, S2):
        # 完整的KMP算法：根据next前缀函数
        n = len(S1)
        m = len(S2)
        i, j = 0, 0
        next = getNext(S2)
        while i<n and j<m:
            if j==-1 or S1[i] == S2[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == m:
            return i-j
        return -1


def getNext(pattern):
    # 获取模式串的next数值.如果p[j] = p[k].则next[j+1] = k+1.否则一直递归k=next[k].直到p[k]=p[j]或者k=0(这个地方的边界条件还是需要清晰一些的)
    m = len(pattern)
    next = [0] * m
    next[0] = -1
    k = -1
    j = 0
    while j < m-1:
        if k==-1 or pattern[j]==pattern[k]:
            j+=1
            k+=1
            next[j] = k
        else:
            k = next[k]
    return next

# 可以自己思考下，next[i]函数的意思就是，当前(下标为i)字符的前面所有字符的最长公共前缀后缀。
# 由此可以搞清楚流程：


if __name__ == "__main__":
    h = "sadbutsad"
    n = "sad"
    n2 = "ababab"
    n3 = "abaabcac"
    pattern = "ABCDABD"
    pattern1 = "abaabcac"
    s = Solution()
    result = s.strStr2(h, n)
    print(result)
    # next = s.strStr4(n3)
    next = getNext(n)
    print("前缀函数", next)
    result1 = s.strStr4(h, n)
    print(result1)