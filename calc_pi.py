# 莱布尼茨求π方法


s = 0
p = 1
num = int(input("输入计算次数："))
for i in range(1, num, 2):
    s = s + 1 / (i * p)
    p = p * (-1)
print(4 * s)
