# 输入一串数字，统计每个数字出现的次数，统计奇偶数出现的次数

nums = input('Enter a list of numbers')
cnt1 = {}
cnt2 = {}
cnt2['Even'] = 0
cnt2['Odd'] = 0

for c in nums:
    if c in cnt1: # 如果数字已经出现，则它的统计次数 +1
        cnt1[c] += 1
    else: # 否则，设为 1
        cnt1[c] = 1
    if int(c) % 2 == 0:
        cnt2['Even'] += 1
    else:
        cnt2['Odd'] += 1

print(cnt1)
print(cnt2)