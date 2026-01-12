num = input("输入一个整数")
num = int(num)
print(num)
oushu = list()
for i in range(num+1):
    if i%2 == 0:
        oushu.append(i)
print(oushu)