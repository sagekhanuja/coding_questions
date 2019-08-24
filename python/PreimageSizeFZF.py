'''
Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)
For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. 
Given K, find how many non-negative integers x have the property that f(x) = K.
'''
def preimageSizeFZF(K):
        """
        :type K: int
        :rtype: int
        """
        temp = K
        count = 1
        while(temp>5):
            temp = temp/5
            count+=1
        tt = K
        b = 1
        for j in range(1,count+1):
                b +=5**j
                
        for i in range(count, 0, -1):
            
            tt = tt%b
            if(b-tt == 1):
                return 0
            b = b-(5**i)
            
        return 5
