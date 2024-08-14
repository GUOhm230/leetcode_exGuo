"""
线性表的相关知识
一. 顺序表
顺序表可讲的不多，顺序表就是用一块连续的内存去存储数据。但是这样的方式也有两种
1）连续的数据存储的就是数据，
2）连续的数据存储的是数据的地址，而真实的数据则是分散存储的，这种称之为元素外置顺序表
以上两种方式都可以做到在访问和尾部插入元素时的时间复杂度为O(1),
在头部或者中间插入，以及删除元素则需要移动元素，在插入时，插入后面的元素需向后移动一位，删除则需要向前移动，因此时间为O(n)
存储了表头信息的顺序表的结构也是有两种实现方式：
1）一体式结构，表头和数据区是紧挨着的
2）分离式结构，表头和数据区分离，因此表头还需要存储数据区开始的位置，也就是L[0]位置
还有一个要注意的就是，数据的扩充与替换，由于顺序表中元素是按照顺序存储，因此计算机分配内存的时候是根据元素个数和长度进行分配的
如果插入元素的话，需要增加内存，这便是动态存储：
1）每次扩充固定数目的内存
2）每次成倍扩充内存
python中的列表和元组均为顺序表结构。
List中，L = [1, 2, 3, 4]中数据为顺序存放，但是如果L = [1, 2.2, 3, 4]

二. 链表
链表，顾名思义，就是用链子链接在一起的表，这个链子是啥呢？就是地址区，前一个元素的地址区，指向后一个元素。
链表的目的是为了利用离散的存储空间，同时，方便在头部插入元素，但是访问以及尾插的时间复杂度都是O(n)
链表的情况比较多：单链表，单向循环链表，双向链表，双向循环链表。主要的问题是操作怎么写，接下来一个小时，我可能都要做这件事，需要高度专注
"""
print("--------------------------------一：顺序表------------------------------------")
L = [104, 1.1, 102, 103] # 其中整数的地址是连续的，因为python中给这些常用整数放了固定的位置，这不受列表的限制。但是非整数的字符串地址则非连续
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(L[3]))
print(id(103))

print("----------------------------------二：链表------------------------------------")
# 1. 单链表
# 1.1 单链表节点定义：数据区以及指向下一个节点的地址
class SingleLinkNode(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None # 创建节点时，并不确认其指向

# 1.2 单链表的相关操作
class SingleLinkList:
    # 初始化单链表，初始化为空,但是需要设立个头指针，这个指针指向头结点，根据python语言特点，意思就是这个头指针储存的是这个头结点的地址，python
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self, item):
        # 链表判空：self.head指向None即为空列表,空则返回True，否则返回False
        return self.__head is None

    def search(self, item):
        # 查找值为item的节点，找到返回True，否则返回False
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            cur = cur.next
        # 中间情况之后考虑特殊情况：查找节点为头，尾，空链表，只有一个节点的情况
        # 假如为空链表:通过；查找为尾结点：通过；查找为头结点：通过，；查找只有一个节点：通过
        return False

    def travel(self):
        # 遍历整个链表
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    def length(self):
        # 返回链表长度。
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        # 头插法：无需两个指针
        node = SingleLinkNode(item)
        node.next = self.__head
        self.__head = node
        # 空指针，也满足

    def append(self, item):
        # 尾插法
        node = SingleLinkNode(item)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        # 某个位置插入
        # 要建立两个指针，因为前一个节点要更改指向
        node = SingleLinkNode(item)
        if pos <= 0:
            self.add(item)
            return True
        else:
            count = 0
            cur = self.__head
            prior = None
            # 先找到pos位置
            while cur is not None:
                # 找到要插入的位置，之后退出循环
                if pos == count:
                    node.next = cur
                    prior.next = node
                    return True
                else:
                    prior = cur
                    cur = cur.next
                    count += 1
            self.append(item)
        return True
        # 这里有两个问题：头插和尾插不行了，所以先设定一下

    def insert2(self, pos, item):
        # 插入节点，这里用老师给的例子，之前的做法比较麻烦
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = SingleLinkNode(item)
            count = 0
            cur = self.__head
            while count < pos-1:
                cur = cur.next
                count += 1
            # 循环完，cur指示的就是pos-1的位置
            node.next = cur.next
            cur.next = node # 可以发现，用不到prior节点，因为插入的是一个节点，而可以知道前一个节点就行了
            # 考虑插入的是头结点，pos=0的情况,插入的是头结点的话，也要考虑原链表为空的情况

    def remove(self, item):
        # 删除某个元素:需要两个指针，因为删除的上一个元素需要重新指向下一个元素，而上一个元素无法从当前元素中获取
        cur = self.__head
        prior = None
        while cur is not None:
            if cur.elem == item:
                if cur != self.__head:
                    prior.next = cur.next
                else:
                    self.__head = cur.next
            else:
                prior = cur
                cur = cur.next
        # 特殊情况：空链表的话，那直接报错,删除的是头结点，删除的是尾结点

# ++++++++++++++++++++++++++++++++++++2. 单向循环链表+++++++++++++++++++++++++++
# 单向循环链表的节点和单链表的节点没有区别，但是链表的构造有一定的区别，就是尾结点与头结点要相连
# 2.1 节点定义:等同于单向循环链表
# 2.2 相关操作
class SingleRecycleLinkList(object):
    def __init__(self, node=None):
        # 初始化单向循环链表：若非空，则要注意循环一下
        self.__head = node
        if node:
            node.next = self.__head

    def is_empty(self):
        # 链表判空
        return self.__head is None

    def travel(self):
        # 遍历循环链表
        if self.is_empty(): # 如果是空链表的话，不打印
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 但是有几种特殊情况：如果为空节点，应该打印None.2. 循环到结束为cur.next，所以最后结束循环的时候是指向最后一个节点
        print(cur.elem)

    def length(self):
        # 长度
        cur = self.__head
        count = 0
        if self.is_empty():
            return count
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        # 这里结束，指针指导尾结点，那么尾结点就没有加上
        count += 1
        # 考虑特殊情况：空链表,返回0
        return count

    def add(self, item):
        # 头插法
        node = SingleRecycleLinkList(item)
        if self.is_empty():
            self.__head=node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head
            # 考虑特殊情况：为空链表:补充，只有一个节点，没有问题

    def append(self, item):
        # 尾插法
        node = SingleRecycleLinkList(item)
        if self.is_empty():
            node.next = self.__head
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node
            # 考虑特殊情况：如果为空，如果仅一个节点

    def insert(self, pos, item):
        # 任意位置插入节点.
        node = SingleRecycleLinkList(item)
        if pos <= 0:
            self.add(item) # 便已经考虑是空链表的事情
            return
        elif pos >= self.length(): # 如果为空链表，这里是可以做到的
            self.append(item)
        else:
            count = 0
            cur = self.__head
            while count < pos-1:
                count += 1
                cur = cur.next
            # 本次循环结束时cur的位置恰是pos-1
            node.next = cur.next
            cur.next = node
            # 考虑特殊情况：如果头插

    def search(self, item):
        # 查找相关节点：这里应该和之前是完全一样的
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            cur = cur.next
        # 一直到这里，没有处理尾结点
        if cur.elem == item:
            return True
        # 考虑下特殊情况：若为空链表，若为单个节点
        return False


def remove(self, item):
    # 删除某个值：这里需要两个指针
    if self.is_empty():
        return
    cur = self.__head
    prior = None
    while cur.next != self.__head:
        if cur.elem == item:
            if cur != self.__head:
                prior.next = cur.next # 如果删除的是头结点，那么prior是没有的
                return
            else:
                # 如果删除的是头结点，那么要重新指向，但是需要找到尾结点，重新指向
                final = self.__head
                while final.next != self.__head:
                    final = final.next
                self.__head = cur.next
                final.next = self.__head
        else:
            prior = cur
            cur = cur.next
    if cur.elem == item:
        if cur == self.__head:
            self.__head = None
        else:
            prior.next = self.__head
    # 这里需要考虑特殊情况：空链表,删除的为尾结点,只有一个节点，删除的即是头结点，又是尾结点,删除的是头结点的情况

# 3. 双向链表，这个看起来会更简单。
# 3.1 节点定义
class DoubleLinkNode(object):
    def __init__(self, elem): # 创建节点的话，肯定是含有元素的
        self.elem = elem
        self.next = None
        self.prior = None

class DoubleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.prior = None # 不用多此一举，因为本来默认就是None

    def is_empty(self):
        return self.__head is None

    def travel(self):
        # 遍历
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next
        # 考虑特殊情况

    def length(self):
        # 长度，与单链表一致
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next
        # 考虑特殊情况：为空链表，一个节点，
        return count

    def add(self, item):
        # 头插法
        node = SingleRecycleLinkList(item)
        if self.is_empty():
            self.__head = node
        else: # 空链表的话，也是符合的，哦，不符合，没有prior这个指针
            node.next = self.__head
            self.__head.prior = node
            self.__head = node
            # 考虑特殊情况：空链表：需要补充

    def append(self, item):
        # 尾插法
        node = SingleRecycleLinkList(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            node.prior = cur
            cur.next = node
            # 尾插法特殊情况：空链表,只有一个节点

    def insert(self, pos, item):
        # 在任意位置插入元素

        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = SingleRecycleLinkList(item)
            cur = self.__head
            count = 0
            while count < pos-1:
                cur = cur.next
                count += 1
            # 结束循环后，指向的就是pos-1位置
            node.next = cur.next
            node.prior = cur
            cur.next.prior = node
            cur.next = node
            # 需要考虑特殊情况了，如果为头插,cur.next是不存在的，因此要排除。如果是尾插，假如长度为3，pos=3,而下标到2，在count=2时不执行，但count=1时是执行的
            # 也就是cur执行最后一个，此时符合，但是如果count大于pos，此时没有cur.next,因此这个时候需要添加的

    def search(self, item):
        # 元素查找
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            cur = cur.next
        return False
    # 考虑特殊情况：空链表，不循环，单节点链表

    def remove(self, item):
        # 删除某个元素：只需要单指针就行了
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                if self.__head == cur:
                    self.__head = cur.next
                    if cur.next is not None:
                        cur.next.prior = None
                else:
                    cur.prior.next = cur.next
                    if cur.next is not None:
                        cur.next.prior = cur.prior
                break
            else:
                cur = cur.next
        # 考虑特殊情况：空链表，直接退出，是没错的。考虑为头结点，因为头结点没有,如果为尾结点，则没有cur.next.prior这个东西
        # 如果既是头结点又是尾结点

# 这里的总结其实主要是一些特殊情况的说明，要考虑哪些特殊情况。这里的代码还是要常看啊

# 给一个单链表：怎么循环插入
# 创建节点
class leetcode_LinkNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# 构造单链表
class leetcode_LinkTabel(object):
    # 在空链表中循环追加节点

    # 这个是错误的，我倒要看看错在哪
    def recurAdd2(self, val):
        head = leetcode_LinkNode(val) # 创建一个单链表
         # 成为第一个头结点
        cur = head
        for i in range(val+1, val+5):
            cur_node = leetcode_LinkNode(i) # 增加一个为当前节点
            cur.next = cur_node
            cur = cur.next
        return head

    def recurAdd(self, val):
        head = leetcode_LinkNode(val) # 创建一个单链表
         # 成为第一个头结点
        cur = head
        for i in range(val+1, val+5):
            cur_node = leetcode_LinkNode(i) # 增加一个为当前节点
            cur.next = cur_node
            cur = cur.next
        return head


if __name__ == "__main__":
    # 测试一下循环添加链表
    ll = leetcode_LinkTabel()
    head = ll.recurAdd(1)
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
    # sll = SingleLinkList() # 创建空链表
    # # sll.append(12)
    # # # sll.travel()
    # # sll.append(13)
    # # # sll.travel()
    # # sll.add(14)
    # # sll.travel()
    # # sll.insert(1, 15)
    # # sll.travel()
    # # sll.insert(4, 16)
    # # sll.travel()
    # # 自己写的插入算法，测试一下
    # # 空链表插入，此时只要insert中有值，便可插入
    # # sll.insert(1, 1)
    # sll.travel()
    # print(sll)
    # print("-------------------")
    # # 只有一个节点插入头结点，以及插入尾结点：此时插入位置>sll.length()同样有效
    # sll.insert(0, 0)
    # sll.insert(3, 2)
    # sll.travel()
    # # 中间位置插入,这里有错误，已经执行完一次，直接break的话，那其实还是执行了后面部分，因此有问题，所以改成return。
    # sll.insert(1, 5)
    # sll.travel()
    # # 那这里其实没有问题了，但是写复杂了
    # print("++++++++++++++++++++++++++2. 单向循环链表+++++++++++++++++++++++++++++++++")
    # slr = SingleRecycleLinkList()
    # slr.travel()