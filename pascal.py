
def generate(numRows):
    pascal = [[1],[1,1]]
    if numRows==0:
        return []
    if numRows == 1:
        return [[1]]
    elif numRows==2:
        return pascal
    else:
        row = 1
            
        
        while row <=numRows-2:
            nums = [1]
            length =2
            valid = pascal[row]
            for i in range(len(valid)-1):
                nums.append(valid[i]+valid[i+1])
            nums.append(1)
            pascal.append(nums)
            length+=1
            row+=1
        print(pascal)
generate(6)
            
                    
                    
                    
                    
                
        