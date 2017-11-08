# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def even_fib(n): # n is the value at each we want to stop the fib sequence
    fib_dict = {}
    fib_dict[1] = 1
    fib_dict[2] = 2
    x = 3
    result = 2
    current = fib_dict[x - 1] + fib_dict[x - 2]
    while current <= n:
        fib_dict[x] = current
        if fib_dict[x] % 2 == 0:
            result += fib_dict[x]
        x += 1
        current = fib_dict[x - 1] + fib_dict[x - 2]
    return result

print(even_fib(4000000))
