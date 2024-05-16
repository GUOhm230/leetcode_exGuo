"""
题目描述: 判断给定的字符串为有效括号
算法思想描述
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        算法思想：
        1. 建立一个字典，存储对应的符号键值对。建立一个空列表
        2. 先排除首个符号为错的情况
        3. 逐个遍历字符串，若该符号不在list中但以该符号为键的值在list中，则从list除去以该符号为键对应的值
        4. 若该符号在list中，则加入list
        5. 遍历完整个字符串，若list不为空，则输出False,否则输出True
        6. 看来思考有问题，并不是需要匹配才行，还必须在匹配时不发生混乱
        这里没有什么要做的，其实就是stack的思想。还是得专业啊。别用list要用stack
        """
        dict = {")": "(", "]": "[", "}": "{"}
        singleList = ["(", "[", "{"]
        list1 = []
        for i in range(len(s)):
            # 存在符号开头为另一半括号的情况
            if s[i] in singleList:
                list1.append(s[i])
            elif not list1:
                return False
            else:
                if dict[s[i]] != list1[-1]:
                    return False
                if dict[s[i]] not in list1:
                    return False
                else:
                    del list1[-1]
        if len(list1) != 0:
            return False
        else:
            return True

if __name__ == "__main__":
    SO = Solution()
    s = "([])"
    s = "]"
    s = "[([]])"
    results = SO.isValid(s)
    print("输出结果", results)
    # list = []
    # print(list[-1])
