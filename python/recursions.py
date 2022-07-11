def collatz(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        return collatz(n // 2, cnt+1)
    else:
        return collatz(3*n + 1, cnt+1)


print(collatz(1, 0))
print(collatz(2, 0))
print(collatz(3, 0))
print(collatz(4, 0))
print(collatz(5, 0))
print(collatz(6, 0))
print(collatz(7, 0))
print(collatz(8, 0))
print(collatz(15, 0))
print(collatz(27, 0))
print(collatz(50, 0))
