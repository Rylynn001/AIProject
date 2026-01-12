f = ""
try:
    f = 1/0
except Exception as e:
    print(e)
print(f)