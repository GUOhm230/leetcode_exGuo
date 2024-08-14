"""
栈和队列
一:栈
栈先进后出，只允许一边对元素进行操作，进出同方向
二：队列
队列先进先出，一边进一边出
栈和队列属于数据结构的一种：存储数据的容器以及相关操作，但是存储数据用啥？python中用列表，其实单链表也是
本处以列表为例
其实两者都属于受限的线性表
"""
class Stack(object):
    def __init__(self):
        self.__stack = []

    def push(self, item):
        # 压栈：从同方向进出，因此考虑时间复杂度，选择从尾部添加，删除
        self.__stack.append(item)

    def pop(self):
        # 退栈：弹出元素，也是从尾部弹出
        if not self.__stack:
            self.__stack.pop()

    def peek(self):
        # 返回栈顶元素
        if self.__stack:
            return None
        return self.__stack[-1] # 不能用self.__stack.pop(),因为这样虽然确实返回了栈顶元素，但是同时改变了栈内容

    def is_empty(self):
        return not self.__stack

    def size(self):
        return len(self.__stack)

class Queue(object):
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        # 入队，这里其实看操作，入队在列表尾的话，那么出队就要时间复杂度O(n)
        self.__queue.append(item)

    def dequeue(self):
        # 出队，但是没说要返回出队元素
        if self.__queue:
            return self.__queue.pop(0)
        return None

    def is_empty(self):
        return not self.__queue

    def size(self):
        return len(self.__queue)

if __name__ == "__main__":
    L = []
    print(not bool(L))
    # L.pop()
    # if not L: # 这是空列表，不是None
    #     print("hahha")
