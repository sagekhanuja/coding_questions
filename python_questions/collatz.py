#model collatz sequence https://en.wikipedia.org/wiki/Collatz_conjecture
def collatz(n):
    iterations = 0
    if n>1: 
        if n%2 == 0:
            iterations+=1
            n = n/2
            print(n)
            collatz(n)
        else:
            iterations+=1
            n = (3*n)+1
            print(n)
            collatz(n)    

collatz(120938102938109238)



