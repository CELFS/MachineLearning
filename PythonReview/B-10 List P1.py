nums = [5, 4, 3, 2, 1]

# 本质并没有修改 nums 的元素，因为 i 是【临时变量】，仅用来存储每次读取 nums 中的一个元素
for i in nums:
    i = i * 2

print(i)
print(nums)