# 表白100天，每天送10朵花
i = 1
while i <= 100:
    print(f"几天是表白的第{i}天")
    j = 1
    while j <= 10:
        print(f"送出第{j}只花")
        j +=1
    if j == 10:
        j = 0
    i += 1