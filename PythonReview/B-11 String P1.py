str1 = '今天天气非常非常的好'
str2 = '天气'

while True:
    delete = str1.find(str2) # 若查到，返回索引值首地址
    # 查找，不存在，返回 -1，中断循环
    if delete == -1: # 替换之后就查不到了，退出循环
        break
    # 查到，执行以下代码
    str1_front = str1[:delete] # 恰好可以用右边开区间来定义范围
    str1_back = str1[delete + len(str2):]
    str1 = str1_front + str1_back
    print(str1)