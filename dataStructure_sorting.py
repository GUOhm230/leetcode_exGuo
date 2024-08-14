"""
排序算法
本章非常重要，接下来的40分钟，我要完成前4个算法
1. 冒泡排序：就是冒着泡，让一个个元素浮在头部或者沉入尾部，每次冒出来的元素是已经排好的。
"""
from typing import List
# 冒泡排序
"""
算法思想描述一下：
1. 从第一个元素开始，相邻两个元素进行比较，若为逆序则交换位置，直至最后两个元素比较结束，此时，底部元素为最大。这时为第一轮排序
2. 重复上述过程，每一轮都从头部元素开始，每轮参与冒泡的元素为初始序列去掉前面冒泡轮数排序好的元素
"""
def bubbleSort(L:List):
    # 使用的是最大值沉底的思路，或者最小值冒泡的想法
    n = len(L)
    for i in range(n):
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

def bubbleSort2(L):
    # 最小值冒泡的思路,没有问题
    n = len(L)
    for i in range(n):
        for j in range(n-1, i, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
    return L

# 2. 选择排序：选择当前无序子序列中最小的元素和第一个元素交换位置
"""
选择排序的思想是：
从第一个元素开始，比较整个序列，找到最小元素，则与第一个元素交换位置，此为第一轮
第i趟排序就是从第i+1个元素开始，比较后面子序列，找到最小元素，与元素i交换位置
以此类推，直至最后一个元素
所以选择排序也简单：第一层循环是排序轮数，第二层循环是每次排序轮数要做的事：选择最小值，然后交换顺序
"""
def choiceSort(L:List):
    n = len(L)
    for i in range(n):
        min_index = i # 最小值的下标，从开头位置开始
        # 找到当前子序列[i, n-1]的最小元素
        for j in range(i+1, n):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L

# 3. 插入排序：在无需元素中选择第一个元素，以正确顺序插入到已排好序的元素中
"""
插入排序的算法思想：
这个其实有点类似于选择排序，两者都是选择一个元素，但是区别是，选择排序的重点就是选择那个最小的元素，而插入排序中的选择是直接拿，重点是插入，不是选择。
1. 每次选择剩余无序子序列的第一个元素
2. 然后和已排序的子序列进行比较，一直找到小于的位置
3. 插入其中，后面元素移动一位.我感觉这个是最难的
4. 当前元素插入2中找到的位置
这里找到插入的时候，有方法可以做选择：如果从前往后查找，找到了后再做插入，再移动元素，不仅时间复杂度增加，逻辑复杂，排序算法也会不稳定
而由于L[j+1]是要移动的位置，所以从后开始才是正解，边比较，边移动，时间复杂度更低，而且排序稳定
"""
def insertSort(L):
    n = len(L)
    for i in range(1, n):
        curElem = L[i]
        for j in range(i-1, -1, -1): # 后面空一个位置，因此要从本处开始
            if L[j+1] < L[j]:
                L[j+1], L[j] = L[j], L[j+1] # 直接交换顺序，这样就对了把，其实还是思路的问题
            else:
                break # 加上这一句，执行会更快一些


        # for j in range(i):
        #     if curElem < L[j]:
        #         # 这里应该将curElem插入L[j]位置，然后后面的元素后移一位，找到此处
        #         for k in range(i-1, j-1, -1):
        #             L[k+1] = L[k]
        #     L[j] = curElem
        #     break

# 4. 快速排序：顺序选取第一个元素作为基准元素，每趟排序均将序列划分为独立的两个子序列，使得第一个子序列中的元素均小于基准元素，第二个子序列均大于或等于。然后递归处理
# 两个子序列
"""
快速排序算法：有分治法的思想在这，只要涉及分治法，就可以用递归
1. 选取第一个元素作为基准元素，两个指针初始指向序列的头尾元素，然后移动尾部指针，直至找到一个小于基准元素者，将他放到low指示的位置，此时high位置的元素可以认为是空的，low指针左移一位
2. 接着，比较low指针元素，小于等于基准元素则指针左移，大于基准元素则将该元素放至当前high指针指示位置，同时high指针右移
3. 两边指针移动至low=high，因为只要两边相等，该处位置的元素必然已被移走了
4. 本轮移动结束，将基准元素放在low以及high指示的位置
5. 以上为一趟排序，根据基准元素，将新序列分成两份。每份递归求解就好
"""
# 这里是一趟排序的情况, 针对一个列表中的某一段进行排序
def pivotSort(L:List, low, high):
    print("本轮待处理的序列：", L[low:high+1])
    pivot = L[low]
    while low < high:
        print("0:", low, high)
        while low < high and L[high] >= pivot: # 比较high指示的元素，直至找到小于基准元素者
            print("1:", low, high)
            high -= 1
        # 此时high指示为小于基准元素者，这个时候，将这个值移动到low位置，并将low右移一位
        # 其实这里退出有两个概念，就是有可能low==high了，也可能是小于而退出
        if low == high: # 因此这里加入low与high相等的比较，此时相等，根本不用换
            break
        L[low] = L[high]
        low += 1
        # 移动完之后，接着应该移动low处的元素了，而low已经移动一位，此时，可能low已经等于high了，因此还要比较low与high的位置
        # if low>=high: # 那这里其实也不对，因为，这个时候要一直移动low指针，而此时high指针指向的元素正好是小于low的，若未比较两者指针，那么low必然会往前移动至=high+1，所以，需要每次都比较一下low与high
        #     break
        # else:
        while low < high and L[low] < pivot:
            print("2:", low, high)
            low += 1
        if low == high:
            break
        L[high] = L[low] #而这里的退出，也有两个情况：要么low==high了，此时就可以退出了，或者确实是low处元素大于基准值, 如果等于，则循环应该直接退出，而不需要再做处理了
        high -= 1
    # 跳出循环时，low=high, 此时只需要将基准值填入即可
    L[low] = pivot
    # 以上为一轮结束，接下来需要对列表进行递归处理,但是以下的递归的方式并不改变L值，我最终要在原列表上变化顺序
    # 因为python中没有引用传递，都是值传递，因此改变方法
    return low

# 本次可以了，确实完成了
def fastSort(L, low, high):
    if low >= high:
        return
    media = pivotSort(L, low, high)
    print("本次基准元素：", media)
    fastSort(L, low, media-1)
    fastSort(L, media+1, high)

def chuandiTest(L):
    L[-1] = 111
    print(L)

# 5. 二分查找：对有序顺序表进行操作，每次对元素进行二分，再对二分，那么可以用递归，也可以不用
# 返回
def binarySearch(L, item):
    # 二分查找
    low = 0
    high = len(L)-1
    while low <= high:
        mid = (low + high) // 2
        print("本轮：", low, high, mid)
        if item == L[mid]:
            return mid
        elif item > L[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

# 6. 归并排序: 就是逐渐合并的排序，既然要合并，那就要能拆，
"""
1. 将序列逐级对半拆分，直至剩一个元素
2. 之前拆分的部分排序合并，直至合并到只有两组
因此，其实有两大问题
s1: 拆分是对半的，但是需要原路进行排序合并，怎么找到之前拆分的两组元素呢？
a1: 可以对当前元素拆掉之后，立即对他进行合并，但是问题又来了
s2: 当前序列进行拆分的时候是对半拆分，然后这两组需要合并成一组，但是这两组并没有先排序，那应该怎么做呢？
a2: 所以可以仅含2个元素的组进行拆分，再排序合并，再对他的母序列进行合并，这就用到了递归的思想了
"""
def mergeSort(L:List):
    if len(L) <= 1: # 只有单个元素时候，返回
        return L
    n = len(L)
    mid = n//2
    left_List = mergeSort(L[:mid])
    right_List = mergeSort(L[mid:])

    # 上面是拆分成两个列表，接下来对这两个列表做合并
    # 如何对这两组列表进行排序呢.比较left和right指示的元素，较小的元素加入result，然后该位置右移一位，直至其中任何一个指针移动至尽头
    left, right = 0, 0
    result = []
    while left < len(left_List) and right < len(right_List):
        if left_List[left] <= right_List[right]:
            result.append(left_List[left])
            left += 1
        else:
            result.append(right_List[right])
            right += 1
    # 本轮循环结束，此时必有一个已经指示到大于其长度
    result += left_List[left:]
    result += right_List[right:]
    return result


if __name__ == "__main__":
    L0 = [5, 4, 3, 2, 1]
    L = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # bubbleSort2(L)
    # print(L)
    # choiceSort(L1)
    # insertSort(L1)
    # print(L1)
    # # print([i for i in range(9, -1, -1)])
    # for i in range(0, -1, -1):
    #     print(i)
    # L = [1, 2, 3, 4, 5]
    # chuandiTest(L[2:])# L = L[2:]相当于传的是不可变元素。因此有问题
    # print(L)
    # 试试快速排序,测试，顺序，倒序，乱序，空顺序表，是没错的
    # L2 = []
    # L3 = [1, 2, 3, 4, 5]
    # fastSort(L, 0, len(L)-1)
    # print(L)
    # # 二分查找：
    # print(binarySearch(L, 32))
    L2 = [17, 26, 54, 93, 31, 44, 55, 77]
    result = mergeSort(L) # 目前报错，递归栈溢出了
    print(result)
    # print(L[len(L)+1:])