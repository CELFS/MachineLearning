# 异常处理【应该可以用在 TDD 里面，建立一个完善的 TDD 机制】
try:
    print(0 / 0)
except:
    print('Something Wrong')