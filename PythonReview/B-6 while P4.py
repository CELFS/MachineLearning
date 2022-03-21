# Fibonacci Sequence the first 30th numbers
first = 1
second = 1
print(first)
print(second)
cnt = 3
while cnt <= 30:
    tmp = first
    first = second
    second = tmp + second
    cnt += 1
    print(second)