import numpy as np
import time
import math
import sys

if __name__ == '__main__':
    start = time.time()
    args = sys.argv
    n = int(args[1])
    src = np.arange(1, n)
    dest = src[(src % 3 == 0) | (src % 5 == 0)]
    print(dest)
    sum = np.sum(dest)
    print('約数の合計は：{0}'.format(sum))
    print("End")
    elapsed_time = time.time() - start
    print('実行にかかった時間は:{0}'.format(elapsed_time) + "秒")
