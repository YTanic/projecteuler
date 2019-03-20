import numpy as np

def createFibonacci(arr, max):
    x = arr[-2]
    y = arr[-1]
    if x + y < max:
        arr.append(x + y)
        createFibonacci(arr, max)

if __name__ == '__main__':
    start = time.time()
    arr = [1, 2]
    MAX = 4000000
    createFibonacci(arr, MAX)
    arr = np.array(arr)
    sum = np.sum(arr[(arr % 2) == 0])
    print('sum is %d' % sum)
    print('約数の合計は：{0}'.format(sum))
    print("End")
    elapsed_time = time.time() - start
    print('実行にかかった時間は:{0}'.format(elapsed_time) + "秒")
