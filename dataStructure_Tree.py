"""
树：树是一种数据结构，至于这个数据结构用什么容器实现，其实可以用顺序表，但是用顺序表，其中左右节点就需要计算或者存储了，不现实
1。 树的相关概念：根结点，父节点，子节点，兄弟节点。祖宗节点，子孙节点。节点的度，树的度，树的深度，森林
2. 树的分类：无序树与有序数
有序数又分：二叉树，霍夫曼树，B树。
二叉树又分：完全二叉树，满二叉树，平衡二叉树，排序二叉树
完全二叉树又很多特征：节点的特征，这些都可以看数据结构的书籍
现在主要是构建二叉树以及二叉树的遍历
以下其实一直说明，我对类和对象的使用，不够灵活，还是要多用
广度优先遍历
所谓广度优先遍历，就是从头开始，然后该节点的左右节点全部遍历一遍，直至没有节点
"""
from dataStructure_StackQueue import Queue, Stack
# 定义树的节点
class TreeNode(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

# 定义树相关操作
class Tree(object):
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        # 完全二叉树添加节点
        node = TreeNode(item)
        if self.root is None:
            self.root = node
            return
        queue = Queue()
        queue.enqueue(self.root)
        while queue:
            curNode = queue.dequeue()
            if curNode.lchild is None:
                # 左孩子不存在，则在此处添加
                curNode.lchild = node
                return
            else:
                # 左孩子存在，则加入队列
                queue.enqueue(curNode.lchild)
            if curNode.rchild is None:
                curNode.rchild = node
                return
            else:
                queue.enqueue(curNode.rchild)

    def BFS(self):
        # 广度优先遍历
        queue = Queue()
        curNode = self.root
        # print(curNode.elem)
        while curNode is not None:
            print(curNode.elem, end = " ")
            if curNode.lchild:
                queue.enqueue(curNode.lchild)
                if curNode.rchild:
                    queue.enqueue(curNode.rchild)
            curNode = queue.dequeue()

    def BFS2(self):
        if self.root is None:
            return
        queue = Queue()
        queue.enqueue(self.root)
        while queue:
            curNode = queue.dequeue()
            print(curNode.elem)
            if curNode.lchild is not None:
                queue.enqueue(curNode)
            if curNode.rchild is not None:
                queue.enqueue(curNode)

    def preOrder(self, root):
        if root is None:
            return
        print(root.elem, end =" ")
        self.preOrder(root.lchild)
        self.preOrder(root.rchild)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.lchild)
        print(root.elem, end =" ")
        self.inOrder(root.rchild)

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.lchild)
        self.postOrder(root.rchild)
        print(root.elem, end=" ")


if __name__ == "__main__":
    t = Tree()
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.BFS()
    print( )
    t.preOrder(t.root)
    print( )

    t.inOrder(t.root)
    print( )

    t.postOrder(t.root)
    # 检测通过




