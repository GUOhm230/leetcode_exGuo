from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 该段代码AC通过。但是时间复杂度较高
        n = len(s)
        # 开始第二轮，暴力解法
        max_Palindrome = ""
        for i in range(n):
            # print("--------------------", i, s[i])
            for j in range(n-1, i, -1):
                if s[i]==s[j]:
                    # print("什么时候相等：",j, s[j])
                    final = j
                    k = i+1
                    p = j-1
                    while k<=p:
                        # print("kp", k, s[k], p, s[p])
                        if s[k] != s[p]:
                            break
                        else:
                            k+=1
                            p-=1
                    if k>p and len(max_Palindrome)<final-i+1:
                        # print("按说到这里了呀")
                        max_Palindrome = s[i:j+1]
                    # print("当前最大字符串：", max_Palindrome)
                else:
                    continue
        return max_Palindrome

if __name__ == "__main__":
    # s = Solution()
    # str = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
    # result = s.longestPalindrome(str)
    # print(result)
    s = "zhangxiwen"
    print(s[0:2])