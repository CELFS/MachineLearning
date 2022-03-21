# Find the max number in the list【我觉得这段代码写得很美，但有无复杂度 log 级别的、。】
l = [3, 14, -5, 42, 98, 5]
max = l[0]
for i in l:
    if max < i:
        max = i
    else :
        continue
print(max)