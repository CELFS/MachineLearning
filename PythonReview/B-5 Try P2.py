try:
    year = int(input('输入你的年份'))
except:
    print('Something Wrong')

# 余数控制索引号
year = (year - 1996) % 12
animal = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
print(animal[year])
