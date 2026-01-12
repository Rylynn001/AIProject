f = open("D:\影视飓风\Text2.txt","r",encoding="utf-8")
count = 0
for i in f.readlines():
    str = i.strip()
    count+=str.count("itheima")
    print(str)
print(count)
f.close()