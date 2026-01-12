def func (name, age, *hobbys, **keywords):
    print(f"我是{name},今年{age}岁,我的爱好有:",end = "")
    # for i in hobbys:
    #     print(i,end = ", ")
    print(",".join(hobbys))
    print(f"我的其他信息: ",end="")
    # for k in keywords:
    #     print(f"{k}=>{keywords[k]}",end = ",")
    info = [f"{k}=>{v}" for k,v in keywords.items()]
    print(",".join(info))

func("黎明", 18, "足球", "篮球", "rap", id=1, height=1.8)