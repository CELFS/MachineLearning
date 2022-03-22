# Exam Practice 3
# 输入一个五位数，判断是不是回文数，例如12321

# 1. 由于数据量较小，可考虑用 list 的 [::-1] 性质，进行翻转
num = input('Enter a five-digit number to judge whether palindrome number: ')

if num == num[:: -1]:
    print('%s is a palindrome number' % num)
else:
    print('%s is NOT a palindrome number' % num)

# 【如果用常规方法，尽可能适应更长的数字，考虑如下思路】
# 1. 根据长度奇偶性,寻找中间元素
# 2. 裁剪为两段
# 3. 由于 Python 列表支持负数索引值，因此可从两端点出发依次判断对应位是否相同
# 4. 如果分两段后数据仍然很长，有两种方法：
#       (1) 考虑再次分割（指针更新）；
#       (2) 通过随机访问提高检索效率.