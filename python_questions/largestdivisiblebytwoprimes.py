
primes = []
for i in range(10_000_000):
    if i % 1000 == 0:
        print(i)
    factors = 0
    for j in range(1, i):
        if i % j == 0:
            factors += 1
    if factors == 1:
        primes.append(i)
print(primes)
            
      