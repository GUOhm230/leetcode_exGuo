"""
题目：罗马数字转成整数
思路：逐渐
"""
def S1(s):
    romanStr = ["I", "V", "X", "L", "C", "D", "M"]
    num = [1, 5, 10, 50, 100, 500, 1000]
    romanNumDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    preS = s[0]
    results = romanNumDict[s[0]]
    print("初始结果：", results)
    strLen = len(s)
    if strLen == 1:
        return results
    for i in range(1, strLen):
        proS = s[i]
        # 并没有这么简单，要分情况讨论
        if s[i - 1] == "I" and (s[i] == "V" or s[i] == "X"):
            results = results + romanNumDict[s[i]] - romanNumDict[s[i - 1]] * 2
            print(i, s[i - 1], s[i], results)
        elif s[i - 1] == "X" and (s[i] == "L" or s[i] == "C"):
            results += romanNumDict[s[i]] - romanNumDict[s[i - 1]] * 2
            print(i, s[i - 1], s[i], results)
        elif s[i - 1] == "C" and (s[i] == "D" or s[i] == "M"):
            results += romanNumDict[s[i]] - romanNumDict[s[i - 1]] * 2
            print(i, s[i - 1], s[i], results)
        else:
            results += romanNumDict[s[i]]
            print(i, results)
    return results

def S2(s):
    romanNumDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ans = 0
    n = len(s)
    for i, ch in enumerate(s):
        value = romanNumDict[ch]
        if i < n - 1 and value < romanNumDict[s[i + 1]]:
            ans -= value
        else:
            ans += value
    return ans

if __name__ == "__main__":
    s = "MCMXCIV"
    s = "III"
    s = "IL"
    s = "IC"
    results = S1(s)
    ans = S2(s)
    print(results)
    print(ans)
    # print("输出数据")
    # for i in range(1, 1+1):
    #     print(i)