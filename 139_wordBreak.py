from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 算法思想:按照长度从头开始遍历字符串。如果长度为1的子串如果在wordDIct中,则继续按照同样的方法遍历子串，直到整个字符串遍历完成.
        # 这个想法是没有问题的，但是不好实现。主要是递归的终止在这里确实有些难度啊。但是这样很符合用动态的思路
        n = len(s)
        dp = [[0]*n]*n
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0 if s[i] not in wordDict else 1
        for L in range(2, n+1):
            print("++++++++++++++L={}+++++++++++++++++".format(L))
            for i in range(n-L+1):
                j = i+L-1
                print("----------------i={}, j={}------------------".format(i,j))
                if s[i:j+1] in wordDict:
                    print("1.匹配成功：", s[i:j+1])
                    dp[i][j]=1
                elif s[j] in wordDict and dp[i][j-1]==1:
                    print("2.匹配成功：", s[j], dp[i][j-1])
                    dp[i][j]=1
                else:
                    k = i+1
                    while k < j:
                        if s[k:j + 1] in wordDict and dp[i][k-1] == 1:
                            print("3.匹配：", i, k, s[k:j + 1], dp[i][k])
                            dp[i][j] = 1
                            break
                        else:
                            print("再来：", k, s[k:j+1])
                            k+=1
                            continue
                print("最终结果：i={}, j={}, dp={}".format(i, j, dp[i][j]))
                print("dp[5][6]={}".format(dp[5][6]))
        print(dp)
        return bool(dp[0][n-1])


    def wordBreak2(self, s, wordDict):
        n = len(s)
        dp = [0]*n
        dp[0] = 0 if s[0] not in wordDict else 1
        for i in range(1, n):
            print("---------------i={}-----------------".format(i))
            # if dp[0] and s[1:i+1] in wordDict:
            #     dp[i] = 1
            #     break
            # if dp[i-1] and s[i] in wordDict:
            #     dp[i]=1
            #     break
            if s[:i+1] in wordDict:
                dp[i] = 1
            else:
                j = 0
                while j < i:
                    print("j={}".format(j), s[j+1:i+1])
                    if dp[j] and s[j + 1:i + 1] in wordDict:
                        dp[i] = 1
                        break
                    j += 1
            print("当前结果：", dp[i])
        return bool(dp[-1])
# 以上没错，但是依然可以优化，增加dp[i]为1的点

if __name__ == "__main__":
    s = Solution()
    str = "catsandog"
    # # print(str[0:3])
    wordDict = ["cats","dog","sand","and","cat"]
    result = s.wordBreak2(str, wordDict)
    print(result)
    # d = {"key":2, "age":3}
    # print(d.keys())
    # if "ages" in d.keys():
    #     print("zai de ")


