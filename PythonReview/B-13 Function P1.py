def num_sum(N):
    sum = 0
    # for i in range(1, N + 1):
    #     sum += i
    for i in range(N):
        sum += i + 1
    return sum

N = int(input('Enter a number, you can get a sum from 1 to N'))

result = num_sum(N)
print(result)