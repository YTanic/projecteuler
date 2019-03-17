import time
import math
import sys

start = time.time()
args = sys.argv
n = int(args[1])
mul1 = 3
mul2 = 5
sum = 0
for i in range(n):
    if i % mul1 == 0:
        sum = sum + mul1
        mul1 = mul1 + 3
    elif i % mul2 == 0:
        sum = sum + mul2
        mul2 = mul2 + 5
print('約数の合計は：{0}'.format(sum))
print("End")
elapsed_time = time.time() - start
print('実行にかかった時間は:{0}'.format(elapsed_time) + "秒")
