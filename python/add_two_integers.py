#problem: add two integers with out using '+'

def add(a,b):
    while b != 0:
        carry = a&b
        a = a^b
        b = carry << 1
    print(a)

add(4,6)