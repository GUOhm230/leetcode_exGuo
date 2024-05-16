"""回文数"""
class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        思想也很简单。就是首尾数字相同
        """
        l_num = len(str(x))
        # if l_num == 1:
        #     return True
        flag = True
        for i in range(l_num, int(l_num / 2), -1):
            high = int(x / (10**(i-1))) # 求高位数字
            low = x % 10**(l_num - i + 1)  # 求低位数字
            # 得到的数字也取其中头尾
            high_len = len(str(high))
            high_l = int(high%10)
            low_h = int(low/(10**(high_len-1)))
            if high_l != low_h:
                flag = False
        return flag

    def S2(self, x):
        """
        方法二：取出一半进行数字翻转，然后比较两边数字是否相同
        :param x:
        :return:
        """
        num2str = str(x)
        l_num = len(str(x))
        h = l_num/2
        return num2str[:h] == num2str[-1:-h-1:-1]

if __name__ == "__main__":
    x = 123
    num2str = str(x)
    print(num2str[-3])
