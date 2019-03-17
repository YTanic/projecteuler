import math
n = int(input())
prime = 2
while n > 2:
    if n % prime == 0:
        n = n / prime
    prime = prime+1
print(prime-1)
print("End")
