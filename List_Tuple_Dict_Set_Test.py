"""
列表，元组， 字典, 集合测试
"""
import time
import os
"""
一： 列表测试
1. 列表性质
1）列表中元素可以是任何类型的：字符串，数字，元组，字典等等.
"""
print("----------------------1. 列表--------------------")
# 增删改查
s1 = [0, "guo", {"name":"guo", "age":19}, (1, "zhang"), {1, 2, "hahah"}]
print(s1)
s = [0, 1, 2, 3, 4]
print("==================列表：增======================")
# 1. 查找访问：用下标索引访问

# for i in s:
#     print(i)
# for i in range(len(s)):
#     print(s[i])
# 切片访问
print(s[2:5])
print(s[::2])
print(s[::-2])
print(s[:-2])
print(s[:]) # 用一个冒号也行s[start:end+1:step] step算的话，就两个冒号，默认没有，就一个冒号
print(s[::])
print(dir(s)) # 列表内置函数
# list.index()：返回某个值的索引下标
print(s.index(2))
# print(s.index(7)) # 如果值不存在会报错
# s.count(2) 返回某个元素在列表中出现的次数
print(s.count(1))

# 2. 改：以索引方式修改，也可以切片修改

# 3. 增：list.append(), list.extend(), list.insert()，+， *
l2 = [5, 6, 7]
print(l2+s) # 两个列表相加，结果是其中的元素按顺序拼接。和extend()功能相同
s.append(l2) # 直接把l2当作元素，加入列表末尾
print(s)
s.extend(l2) #扩展列表：把l2列表中的元素逐个加入列表末尾
print(s)
s.insert(0, l2) # 在对应位置插入l2这个元素，而不论这个元素是列表还是啥
print(s)
print("=================时间测试=========================")
# 测试下时间
t1 = time.time()
l3 = [i for i in range(10000)]
l6 = l3.copy()
l7 = l3.copy()
l8 = l3.copy()
t2 = time.time()
print("t=",t2-t1)
l4 = [j for j in range(10001, 20000)]
t3 = time.time()
print("创建列表好耗时：",t3-t2)
l5 = l3+l4
t4 = time.time()
print("+连接耗时=",t4-t3, len(l5))
l6.extend(l4)
t5 = time.time()
print("extend耗时=",t5-t4,l6==l5)
for j in l4:
    l7.append(j)
t6 = time.time()
print("append耗时=",t6-t5, l7==l6)
for j in l4:
    l8.insert(len(l4), j)
t7 = time.time()
print("insert耗时=", t7-t6, l8==l7)
l9 = [1, 2, 3]
l10 = [4, 5, 6]
for k in l10:
    l9.insert(len(l10)+1, k)
print(l9)
# 总结一下：四种增加值的方法里，+和extend()方法耗时很少，append()稍多一些。insert则很长。
# 4. 删:list.remove(值)， list.pop(index)：默认删除末尾元素，也可以指定删除特定索引的元素， lr.clear():清空列表, del lr[index]或者切片
lr = [5, 6, 7, 8]
# del lr[2:]
# print("del删除：", lr)
lr.remove(5)
# lr.remove(9) # 该值需要存在,
print(lr)
lr.insert(0, 5)
print(lr)
lr.pop()
print(lr)
lr.pop(0)# 输入index
print(lr)
lr.clear()
print(lr)


print("-----------------------------------2.元组---------------------------------------------")
"""
2. 元组：不可变类型，可哈希,frozenset(s3)冻结的集合也是不可变类型，可哈希。列表，字典，集合均可变类型，不可哈希
元组用()表示
元组不能修改，也就是说元组无法增和改以及删.
可以查，可以用下标访问
别和集合混了，集合不能用下标访问，但是可以增，删，改
"""
# 1. 创建
# 创建空元组
t = ()
print(type(t))
t = tuple()
print(type(t))
# 一个元素的元组,要加逗号
t = (1, )
print(t)
t = ((1, 2), ("guo", "zhang", "hhah"))
print(type((t)))
# 用tuple(list)将列表转成元组
l = [1, 2, 3, [4, 5]]
tt = tuple()
# 元组直接打包创建，甚至不用小括号
t = 1, 2, 3
print(t)

tttt = t.__add__((6,))
print("内部：", tttt)

# 2. 元组的增删改查
# 元组支持下标索引访问查
for i in range(len(t)):
    print(t[i])

print("计数", t.count(1)) # 元组中1的个数统计
print("查找", t.index(1)) # 元组中1的索引
print(dir(t))

# 元组不能增加元素，但是可以通过组合的情况，也就是+连接符进行增加元组，也能用*进行元素复制
t1 = ((60, 80), (70, 90), (100, 120))
# t2 = ((60, 80), (70, 90), (100, 120))
t2 = t1 + t # 下划线应该是元素类型差异
print(t2*2)

# 元组无法删除单个元素，只能删除整个元组
del t2
# print(t2) # 元组删除了，甚至不是变空元组，而是直接抹除了

# 是不可变类型，因此不可改


print("--------------------3. 字典---------------------")
"""
字典太重要了，还是容易出错的地方
1. 字典的创建方式非常多
2. 字典的访问形式非常多样
"""
# 1. 字典的创建
# 1.1 空字典以及直接创建
d = dict()
d = {"name":"guo", "age":18, "sex":"male"}
print(d)

# 1.2 利用元组创建
t = ("name", "guo"), ("age",18), ("sex", "male")
d = dict(t) # 元组转化成字典
print(d)

# 1.3 元组列表联合创建
l = list(t)
print(l)
d = dict(l)
print(d)

# 1.4 两个单列表转元组对，再转字典
key = ["name", "age", "sex"]
value = ["guo", 18, "male"]
t = zip(key, value)
t1 = tuple(list(t)) # 直接t是显示对象，转成列表再转成元组就能显示了
# print("复制：", t1.copy()) 不能使用复制
d = dict(t1)
print("元组列表形式创建字典：", d)
print(tuple(list(t)))
# 执行完tuple(list(t))后，t的内容为空
# 这里需要学到的一点是，经常在数据执行完后，该变量内容就被清除了，所以经常要复制副本

# 1.5 用fromkeys创建只包含键，值为None的字典
d = dict.fromkeys(key)
print(d)
print(dir(d))
d1 = d.copy() #字典可以复制
print(d1)

# 2. 字典访问：d.keys(), d.values(), d.items()
# 2.1 用键访问值：d[键]，但是这里如果是不存在的键则会报错
print(d["name"])
# print(d["lover"])

# 2.2 用get取值更好一些，不存在的键也能用
print(d.get("name", "guo"))
print(d.get("lover", "zhang")) # 输出默认值，但是并不加入字典
print(d)

# 3. 字典值的修改
d["name"] = "guo"
print(d)

# 4. 字典增加元素
# 4.1 增加键值对
d["lover"] = d.get("lover", "zhang")
print("d:", d)
# 4.2 setfault指定键值，如果键存在则改，不存在则加，这点同d[key]=value
d.setdefault("school", "同济大学")
print("setdefault:", d)
# 4.3 使用update进行字典合并：在原字典上修改：同样的键，以第二个为准更新，不存在的键则添加进去
k1 = ["name", "age", "sex", "score"]
v1 = ["guo", 18, "male", (100, 120, 150)]
d1 = dict(zip(k1, v1))
print("d1:", d1)
d.update(d1)
# print("d2:", d2)
print("更新后的", d)
print(d1)

# 5. 字典删除
# 5.1 d.pop(key) 。返回的d删除对应的键值对，整个返回被删除的值
# print(d.pop("hhaha")) #删除不存在的键则会报错
print(d)
# 5.2 d.popitem() 随机删除一个键值对，同样返回被删除的键值对，d为被删后的字典
print(d.popitem())
print(d)
# 5.3 d.clear()直接清空字典
d.clear()
print(d)

print("---------------------------------4. 集合---------------------------")
"""
4. 集合
有关集合需要注意：两大特性：
1）无序性：这就导致了不存在下标访问，既然下标无法访问，自然也不能指定位置查找之类的，和元组列表那样，
2）不可重复性: 重复的元素会被删除
"""
#1. 集合的创建
s = set()
print(s)
s = {1, 2, 3}
print(type(s))
# 列表和元组转化成集合
s = set([1, 2, 3])
print(s)
s = set((1, 2, 3))
print(s)

# 2. 集合的访问，不能用下标进行访问，但是可以使用for循环逐个访问
for i in s:
    print(i)

# 3. 增加集合元素。s.add(elm), s.update(s1)
s.add(4)
print(s)
s.add((2, 4, 5)) # add为在集合中添加括号中的元素，和列表的append的一样，只传入一个值
# s.add([2, 4, 5]) # 不能这样，要放入一个可哈希的数据结构,列表，集合，字典，均不可哈希。元组可哈希。可哈希的话，那么一个周期内，他的
print(s)

s1 = {4, 5, 6, 7}
s.update(s1) # 和dict中的update差不多，有的就不变，没有的加上去，这个才能批量增加元素
print(s)

# 4. 删除元素
s.remove(5) # 删除已存在的值，不存在则报错
print(s)
s.discard(8) # 删除元素，不存在也不报错
print(s)
x = s.pop() # 删除任意一个元素，因为集合是无序的，所以不知道删除哪个，不过一般都是第一个
print(s)
print(x)
# s.clear() # 直接清空之
# print(s)

# 5. 集合的数学运算：交集和并集
s3 = s.union(s1) # 并集
print(s)
s2 = s.intersection(s1) # 交集
print("s2", s2)

# 6. 集合转成不可变集合，这样集合就不能删除修改了
s0 = frozenset(s3)
print(s0)
# s0.add(3)
# print(s0)
# print("==============================5. 写代码时遇到的问题======================================")
# s = "  hello world  "
# sl = s.split() # 以空格划分数据集后，会在多空格处出现空字符串，也就是len(str)==0
# print(sl)
# # 现在问题是怎么删除掉这些空串？
# for i, elm in enumerate(sl):
#     if len(elm)==0:
#         sl.pop(i)
# print(sl)
print("------------------------------5. 字符串-------------------------------------------")
"""
字符串是不可变数据类型
所谓不可变数据类型，就是他不能增删改，但是可以查，字符串可以通过下标访问
"""
# 1. 字符串的定义法有三种：双引号，单引号以及三引号
# 2. 字符串可以通过下标访问查找
# 3. 字符串不能添加元素，但是可以做字符串拼接：+, ().join()
# 4. 字符串有很多其他重要的函数：str.split(), str.strip(), str.rstrip(), str.lstrip()
# 使用默认分隔符
# 默认情况下，split() 函数会使用所有空白字符作为分隔符，包括空格、制表符、换行符等。

print("====================列表循环删除==========================")
L = [i for i in range(8)]
# L = [i for i in L if i % 2!=0] # 可行，就地转
# print(L)
# print(L)
for i in range(len(L)-1, -1, -1):
    print(i, L[i], L)
    if L[i] % 2 == 0:
        del L[i]
        # L.remove(L[i])
        print("hhaha")
print(L)

L = [[1, 2, 3], [4, 5, 6]]
n = len(L)
m = len(L[0])
a = [L[i][j] for i in range(n) for j in range(m)]
print(a)
# print(L[::][2])
# 这样的话，需要找到列表的最大值
m = max([max(L[i][j] for i in range(n) for j in range(m))])
print(m)

se = {1, 2, 3}
se.remove(2) #删除不存在的字符会报错
print(se)
a = 123
print(str(a))
print(list(str(a)))
b = list(str(a))
b.reverse()
print(b)
print(tuple())
print(list())
print(tuple())