def primes_below(n):
    out = list()
    for num in range(2, n-1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            out.append(num)
    return out

print(primes_below(17))