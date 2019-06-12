def kthGrammar(N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        
        if N==1:
            return 0
        if N == 2:
            return 0 if K == 1 else 1
        if K<=2**(N-2):
            return kthGrammar(N-1, K)
        else:
            return 1-kthGrammar(N-1,K-(2**(N-2)))
       