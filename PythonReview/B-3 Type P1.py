money = int(input("How much ?"))
month = int(input("How long ?"))
rate = int(input("What's the rate ?"))

# 【税率、利息，没搞清概念就开始做，结果就是单位错了】
rate = rate / 100
total = money * (1 + rate) ** month
interest = total - money
print(interest)