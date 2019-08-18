## determine if number is a perfect square

##inefficient solution
def perfect_square(num):
    i = 0
    while i**2<=num:
        if i**2 == num:
            return True
        i+=1
    return False

def efficientPerfectSquare(num):
    l,r = 0, num
    while l <=r:
        m = (l+r) >>1
        if m*m == num:
            return True
        else:
            if m * m  < num:
                l = m + 1
            else:
                r = m - 1
    return False

##test           
efficientPerfectSquare(16)