num = 10
if int(input("猜测第一个数字")) == num:
    print("猜中了")
elif int(input("猜测你第二次")) == num:
    print("第二次猜中")
elif int(input("猜测第三次")) == num:
    print("第三次猜中")
else:
    print("楞的呢")