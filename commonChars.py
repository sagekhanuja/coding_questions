#find common characters given array with strings
def commonChars(A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        smallest= min(A)
        common=[]
        distinct=set(smallest)
        for char in distinct:
            minimum=smallest.count(char) 
            for word in A:
                minimum=min(minimum,word.count(char))
                if minimum==0:
                    break
                    
            for _ in range(minimum):
                common.append(char)
                    
        
        return common