"""
学习python链表的相关知识
"""
# python中变量名其实储存的就是数据的地址。而不是别名

# 定义节点类
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    head = list1
    pre = None
    while list2:
        temp = list2
        print("当前所执行的元素", list2.val)
        # while list1:
        #     # 判断数小于等于list1中值则进行在该值前插入节点如果插入的是头节点呢？
        #     if list2.val <= list1.val:
        #         # 如果是头节点则减少一步
        #         if pre == None:
        #             temp.next = list1
        #         # 如果是尾节点，则只需要连接一次即可return.
        #         else:
        #             temp.next = list1.next
        #             list1.next = temp
        #         break
        #     elif list1.next == None:
        #         list1.next = temp
        #         return head
        #     else:
        #         pre = list1
        #         list1 = list1.next
        list2 = list2.next
    return head

if __name__ == "__main__":
    list12 = Node(4)
    list11 = Node(2, list12)
    list1 = Node(1, list11)
    list22 = Node(4)
    list21 = Node(3, list22)
    list2 = Node(1, list21)
    head = mergeTwoLists(list1, list2)
    while head:
        print(head.val, end=",")
        head = head.next
    # list12.next = list21
    # while list1:
    #     print(list1.val)
    #     list1 = list1.next



# a = 10
# b = 20
# print(id(a))
# print(id(b))
# # a=b
# # b=a # 这样做交换是不行的
# a, b = b, a # 而这样直接交换却可以是为啥？
# print(a, b)
# print(id(a))
# print(id(b))