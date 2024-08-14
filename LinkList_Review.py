"""
单链表的复习：最近做有关单链表的题，总是出错
1. 单链表的循环遍历
2. 单链表的边界终止条件：单链表的查找
3. 单链表循环添加元素，也就是创建单链表：头插法创建，尾插法创建
"""
from typing import List
class SingleLinkNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SingleLinkList(object):
    def __init__(self, node=None):
        self.head = node # 该单链表，自然是包含一个头结点的

    def length(self):
        if not self.head:
            return 0
        cur = self.head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        return l

    def travel(self):
        # 循环遍历单链表, 并按元素顺序输出为列表
        result = []
        cur = self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result


    def append(self, val):
        # 尾插法
        node = SingleLinkNode(val)
        if not self.head:
            self.head = node
            return self.head
        cur = self.head
        while cur.next:
            cur = cur.next
        # 经过当前循环后，cur指向尾结点，接下来链接就可
        cur.next = node
        return self.head # 返回节点

    def CreatLinkList_tail(self, L: List[int]):
        # 将单链表的创建放在类中, 经过测试，没有问题
        if not self.head:
            self.head = SingleLinkNode(L[0])
            start = 1
        else:
            start = 0
        cur = self.head  # 指针指向其
        for i in range(start, len(L)):
            node = SingleLinkNode(L[i])
            cur.next = node
            cur = cur.next
        return self.head

    def search(self, elm):
        cur = self.head
        while cur:
            if cur.val == elm:
                return True
            cur = cur.next
        return False

    # 这里还需要改进
    def insert(self, pos, val):
        # 在对应位置插入元素：1. 找到该位置；2. 在对应位置进行修改；3. 注意，要指向插入的位置的前一个元素，也就是指向pos-1的位置
        cur = self.head
        node = SingleLinkNode(val)
        count = 1
        while cur:
            print("cur.val:", cur.val)
            if count == pos:
                break
            cur = cur.next
            count += 1
        print("当前节点值：", cur.val)
        node.next = cur.next
        cur.next = node

def CreatLinkList(L: List[int]):
    # 从空开始创建一个链表，使用头插法
    """
    经测试通过，所以这个单链表的插入应该相对清楚了把
    step1: 要创建单链表，则自然要创建一个头结点
    step2: 要将节点一个个连接，则需要每次将指针指向当前的尾结点，然后在尾结点处插入一个元素
    step3: 每次循环到一个数字时，应当创建该节点
    step4: 节点链接：当前cur指针的next指向当前定义的节点
    :param L:
    :return:
    """
    head = SingleLinkNode(L[0]) # 创建一个头结点
    cur = head # 指针指向其
    for i in range(1, len(L)):
        node = SingleLinkNode(L[i])
        cur.next = node
        cur = cur.next
    return head

def CreateLinkList_head(L: List[int]):
    # 从空开始创建单链表，但本次使用头插法
    # 其实头插法和尾插法差不多，主要是链表的连接我今天总是搞得迷迷糊糊
    head = SingleLinkNode(L[0])
    for i in range(1, len(L)):
        node = SingleLinkNode(L[i])
        node.next = head
        head = node
    return head

if __name__ == "__main__":
    L = [i for i in range(6)]
    head = CreatLinkList(L)
    sl = SingleLinkList(head)
    result = sl.travel()
    print(result)

    head2 = CreateLinkList_head(L)
    sl2 = SingleLinkList(head2)
    result2 = sl2.travel()
    print(result2)

    # 每次都调用一次头插法，同样可以做到生成一个单链表
    sl3 = SingleLinkList()
    for i in L:
        sl3.append(i)
    result3 = sl3.travel()
    print(result3)

    # 如果放在类中呢？这个方法应该怎么做
    sl4 = SingleLinkList()
    head4 = sl4.CreatLinkList_tail(L)
    # result4 = sl4.travel()
    # print(result4)
    #
    # print(sl4.search(0))
    # print(sl4.search(7))
    # print(sl4.search(3))

    # 插入一下
    sl4.insert(1, 6)
    result5 = sl4.travel()
    print(result5)

    LL = [1, 2, 3]
    LL.remove(1)
    print(LL)

    s = "1"
    print(dir(s))
    print(s.isdigit())