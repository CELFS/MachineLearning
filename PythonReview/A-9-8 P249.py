a = 5

# a 比 1 大，而且 a 比 10 小
# 这样写，需回到 Python 是否有隐式类型转换机制
logic_and = 1 < a and a < 10
print(logic_and)

# a 比 3 大，或者 a 比 1 小
logic_or = a > 3 or a < 1
print(logic_or)

# String
logic_string = '1 < a and a < 10'
print(logic_string)