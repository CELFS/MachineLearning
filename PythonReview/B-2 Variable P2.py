# B - Practice codes from https://tianchi.aliyun.com/course/260/3129

# flip a number of four digits
num = 1234
carry = 3
sum = 0
while num % 10:
    n0 = num % 10
    num = (num - n0) / 10
    # 获取当前 num 位数，以控制单词 sum 的乘积倍数
    sum = sum + n0 * (10 ** carry)
    carry -= 1

print(int(sum))
