"""
1. 列表
2. 元组
3. 字典
4. 集合
5. 字符串
"""
print("================================1. 字典===========================================")
# 1. 字典创建
# 空字典：dict()。
# 列表===>zip元组====》字典
l1 = [1, 2, 3, "name", "age"]
l2 = [4, 5, 6, "Ghm", 6]
z1 = zip(l1, l2)  # 也是一个迭代器，当这个迭代器已经执行了一次for也就是运行了一次next()的时候，该迭代器就为空了。
# z2 = z1.copy()  # 没有copy这个东西
# for e in z1:
#     print(e)
d1 = dict(z1)
t1 = tuple(z1)  # 上面已经运行了一次，这次还要再使用此时z1中的值便为空了，于是t1为空。 于是最好还是用tuple(zip(l1, l2))
print(z1)
print(d1)
print(t1)

# 2. 字典的遍历.keys(), .values(), .items()。
for key in d1.keys():
    print(key)
print(d1.keys()) # 并非列表格式，不是列表类，而是class dict_values
print(d1.values())
print(d1.items())
# 用in判断某元素是否存在于内
a = 6
# 这样的判断是判断当前值是否为字典的键等价于if a in d1.keys().
if 4 in d1:
    print("元素在里面")
else:
    print("元素不在其内")

if a in d1.values():  # 值可能是存在多个同样值得
    print("该值在values中存在")

# 通过值拿到键
dv = d1.values()
dk = d1.keys()
di = d1.items()
print(type(dv))  # <class 'dict_values'>
print(type(dk))  # <class 'dict_keys'>
print(type(di))  # <class 'dict_items'>
print(dir(dv))  # 可以发现，以上这些数据并不对外提供数据处理的方式，可以for循环，是个可迭代对象，应该可哈希
print(type(list(dv)))  # 这样转成list，才能用list的一些函数
indexes = [index for index, elm in enumerate(list(dv)) if list(dv)[index] == a]  # 所以，列表的index()只返回最先出现的那个
print(indexes)  # {1: 4, 2: 5, 3: 6, 'name': 'Ghm', 'age': 6}
keys = [list(dk)[index] for index in indexes]  # 这样就能获取到值对应的键了
print(d1)
print(keys)
# print(list(dk)[indexes])  # 通过值去获取对应的键：取出
print(dir(list(dv)))

# 3. 键值得获取，查询
a = d1["name"]  # 通过这个方式获取的值，如果键给的是错误的
print(a)
b = d1.get("sex")  # 可以通过这个方式取得键对应的值，如果键不存在，则会输出默认值
print(b)

# 4. 增加键值对或者修改键值对
print(d1)
d1["sex"] = "female"  # 可以直接增加键值对：如果键存在，则修改，键不存在则添加进去。
print(d1)
d1["score"] = d1.get("score", 70)  # 这里就有个好处了，原来存在这个值得话，就不用更新，不存在的话，就增加这个键，然后更新
print(d1)
d1.setdefault("name", "同济大学")  # 同样是，存在则无需操作，不存在则添加
print(d1)
#  综上，三种增加键值对的方法，要修改就用d1[key] = value.要增加就用后面两个，这两个不存在修改本就存在值的功能

# 看看他fromkeys:之前一直以为没用，结果可以用来给列表去重，且保证列表顺序
ld = list(range(5))
d2 = dict.fromkeys(ld)
print(d2)
print(list(d2))
print(list(d2.keys()))  # 上面两种方式效果一致。
print(list(d1))

# 5. 字典的删除
d1.pop("name")  # 删除特定的键值对，不存在的键会报错,返回被删除键的值
print(d1)
k, v = d1.popitem()
print(k, v)
print(d1)  # 随机删除，并返回被删除者
# d1.clear()  # 直接清空字典
# print(d1)
"""
总结一下：
1. 字典的创建：利用元组创建。元组可以通过列表用zip创建.
2. 字典的遍历：.keys(), .values(), .items()。这些生成的不是list，但是可以直接转成list。
3. 查询：a in d。是查询d中是否有名为a的键。如果要通过值去查询键，那么就要先得到值得list，然后查询list中对应的值，找到其索引，然后取keys的列表中找到对应的keys.
# keys和values的联系除了可以通过键访问值，也能通过键值分别的列表获取对应的索引，来得到其值
4. 键值的修改与添加d[key]=value:有则改无则加。d[key]=d.get(key, value):有则不操作，无则改。d.setdefault(key, value):有则无需操作，无则改
5. 字典的删除：d.pop()删除指定的键，d.popitem()随机删除
6. 字典合并：d1.update(d2):两个字典，改变d1：有的话则更新，无得话则添加
"""
L1 = ["name", "age"]
L2 = ["guo", 17]
print(tuple(L1))  # 一个列表并不能直接转成元组对
print(dict(tuple(zip(L1, L2))))
rm = d1.pop("age")  # 返回被删除的键的值
print(rm)

print("=============================================2. 集合======================================================")
"""
集合的特性：无序，不可重复
无序：不可通过下标访问，且list转成set，再重新变成list，可能导致list中元素位置发生变化。要不变，用list(dict.fromkeys(l))
不可重复性：重复的元素会被删除
"""

# 1. 字典的创建以及list转字典。创建空集合要用s = set().s = {}是创建空字典
# 2. 集合的添加
ll = [1, 2, 3, 4, 5]
s = set(ll)
print(s)
# s.add([6, 7])  # 不能使用不可哈希的可迭代对象，列表不可哈希
print(s)
s2 = set([4, 7, 8, 9])
s.update(s2)  # 和dict的update一致。有则不变，无则加。
print(s)
# 3. 集合的删除
s.remove(5)  # 删除指定的元素，若该元素不存在，则报错
print(s)
s.discard(10)  # 删除指定的元素，若该元素不存在，也不会报错
print(s)
x = s.pop()  # 一般是删除第一个，但是集合是无序的，因此也可能删除其他位置的
print(x)
# print(s.clear())  # 直接清空元素
# print(s)

# 4. 集合的访问：集合可以访问其长度,有min, max, sum
print(len(s2))
print(min(s2))
print(max(s2))
print(sum(s2))
print(s2)
# print(s2.count(4))  # 没有count，没有index函数了
print(dir(s2))
# 可以通过循环访问输出，但是不能通过下标访问。
# for elm in range(len(s2)):
    # print(s2[elm])
# 4. 集合的交集和并集
s0 = frozenset(s2)  # 集合本就是可变类型，所谓可变类型是指可以增删改。将集合变成不可变类型，就可以哈希了，但是不能再修改了
s.add(15)
s2.add(17)
print(s)
print(s2)
s3 = s.union(s2)  # 求出并集,返回一个新的并集。并不会在原来的集合上返回
print(s)
print(s3)
s4 = s.intersection(s2)  # 获得交集，同样是返回一个新的交集，不会在原来的集合上返回。
print(s4)
print(s)
print(s2)
print("===================================3. 字符串===============================================")
"""
字符串是不可变类型
因此无法进行增删改。但是可以链接
"""
# 1. 字符串的访问：可以下标访问，一切正常访问的为单个字符，
str1 = "        guo hui  ming    hha "
str2 = "guo_hui_ming_"
for i, char in enumerate(str1):
    print(char, str1[i])
print(dir(str1))
# 2. 字符串切割
sl1 = str1.split()  # 默认空格， 前后有空格的话，或者tab键，都会包含在内
print(sl1)
sl2 = str2.split("_")  # 注意， 这里如果以其他的为分隔符的话，会有一些""，这种出现在这个字符后面没了，或者连续的两个分割符的情况
print(sl2)

# 3. 字符串大小写：全大写，全小写，仅首字母大写。均需要左边赋值，因为字符串为不可变类型，因此不可在原地修改
str3 = "guo Hui ming"
str7 = str3.upper()   # 转换成全大写的方法
print(str7)
str4 = str3.capitalize()  # 首字母大写形式，后面的字符有大写的也会变成小写
print(str3)  # 不可变类型，因此不能在原位置上进行修改。
print(str4)
str6 = "GUO HUI Ming"
str5 = str6.lower()  # 将所有字符变成小写，同样的，需要重新赋值
print(str5)

# 4. 字符串的其他操作
# 移除空白字符就不提了：str.strip()    str.lstrip()    str.rstrip()
index = str5.find("hii")  # 返回字符串中，括号中字符元素第一次出现的位置。其中括号内元素可以是子串。未找到返回-1
print("find:", index)
num = str5.count("ui")  # 返回某个字符或者字符串出现的次数
print(num)
# 以上两个方法均可以指定字符串的起始位置
print("str5长度：", len(str5))
num2 = str5.count("g", 0, 12)
print(num2)
print(str5.index("g"))  # index也是查找子字符串所在的位置，未找到则抛出异常.而find则返回-1

# 5. 判断数字与否
sn = "Ⅳ"  # 这个罗马字符还不是IV这样写出来的。
print(sn.isdigit())  # 判断数字与否，只能是正整数字符。直接返回bool
print(sn.isnumeric())  # 判断数字与否:正整数，罗马字符等，直接返回bool
print(str5.startswith("ga"))  # 是否以指定前缀开始
print(str5.endswith("ing"))  # 是否以指定后缀结束
print("guo中_国人".isalpha())  # 检测是否只包含字母：英，中都算。数字，空格符号啥的就不算
print("hakahk".zfill(5))  # 填充0,使字符串达到指定长度，如果本身长度就超过括号里的，那就不填充了，保持源输出
print(str5.title())  # 字符串中每个单词首字母均大写






