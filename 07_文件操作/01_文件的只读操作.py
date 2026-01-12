# f = open("D:\影视飓风\Text.txt", "r", encoding="utf-8")
# lst = f.readlines()
# # lst = lst.strip()
# for line in lst:
#     print(line.strip())
# f.close()
with open("D:\影视飓风\Text.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())