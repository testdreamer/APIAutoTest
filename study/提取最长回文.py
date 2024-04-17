# _*_ coding : utf_8 _*_
# @Time : 20:01 
# @Author : 田霄汉
# @File : 提取最长回文
# @Project : APIAutoTest
# @User : Administrator


s = 'dajdsaiqwqiaaiqloijknda'

def is_palindrome(s):

    return s == s[::-1]

res_list = []
for i in range(len(s), 0, -1):
    for j in range(0, i):
        # print(s[j:i])
        if is_palindrome(s[j:i]):
            res_list.append(s[j:i])
        else:
            pass
print(max(res_list, key=len))