def func(name,**kwargs):
    for k, v in enumerate(kwargs):
        print(k+"=>"+v)
    print(type(kwargs))

print(func("小明",id = 1))


