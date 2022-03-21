import time

# n = 5
# while n > 0:
#     print(n)
#     time.sleep(1)
#     n -= 1
# print('Blastoff')
# print(n)

while True:
    line = input('> ')
    if line == 'quit':
        break
    if line == 'sleep':
        continue
    print(line)
print('Out of the while')