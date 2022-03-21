# B - Practice codes from https://tianchi.aliyun.com/course/260/3129

# Swap the values of two numbers
# 未涉及深浅拷贝问题
# 交换的本质，是 Knuth 书中讲到的，一个空出来没用了，可以直接使用它其他用途（除非名称有含义）
num1 = 10
num2 = 5
num3 = num1
num1 = num2
num2 = num3
print(num1, num2)
