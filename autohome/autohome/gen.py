def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b

        n = n + 1
        # print(b)
    return 'done'

f= fib(20)
for f in f:
    print(f)



