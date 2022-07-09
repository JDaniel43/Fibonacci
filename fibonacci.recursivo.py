def fib_r(n):
    if n  < 2:
         return n
    else:
        return fib_r(n-1) + fib_r(n-2)     
for x in range (10):
    print(fib_r(x))