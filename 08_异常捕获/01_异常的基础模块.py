try:
    f = open("D:\影视飓风\Text.txt","r",encoding="utf-8");
except:
    print("没有这个文件")
    f.close()
print(f.read())
print("程序运行完成")
f.close()

