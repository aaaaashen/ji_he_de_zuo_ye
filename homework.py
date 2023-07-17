#计算总和
count = 0
for i in range (1,10):
    count+=i
print(count)

#100个和尚吃100个馒头，其中一个大和尚三个馒头，三个小和尚一个馒头

for a in range (0,100):
    if a*3+(100-a)*(1/3) == 100:
        print("有%d个大和尚，%d的小和尚"%(a,100-a))
        pass
    pass


#指定列表，并找出只出现过一次的数字
li=[1,2,3,2,4,3,5,7,5,4]
for i in range (1,10):
    if li.count(i)==1:
        print(i)
        pass
pass