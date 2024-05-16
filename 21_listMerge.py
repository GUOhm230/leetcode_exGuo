"""
题目描述：整合两个已经排好序的list。
这道题难得不是怎么做出来以及算法思想，难的是官方怎么表达的列表节点的。根本不知道啥意思啊
所以本处的问题：
有关python的数据结构算法需要学习一下
"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if min(len(list1), len(list2)) == 0:
            return list1 + list2
        results = list1
        for i in range(len(list2)):
            for j in range(len(list1)):
                if list2[i] <= list1[j]:
                    results.insert(j, list2[i])
                    break
                if j == len(list1) - 1:
                    return results + list2[i:]

        return results

if __name__ == "__main__":
    SO = Solution()
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    print(l1.val)
    # l1 = []
    # if not l1:
    #     print("空列表也算？")
    # l1 = []
    # l2 = []
    # results = SO.mergeTwoLists(l1, l2)
    # print(results)