def compute(x,y):
    return x+y
def test(compute):
    return compute(2,3)


print(test(lambda x, y: x + y))
print(test(lambda x, y: x - y))
print(test(lambda x, y: x * y))
print(test(lambda x, y: x / y))