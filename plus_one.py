'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = True
        for i in reversed(range(len(digits))):
            digits[i] += 1 if carry else 0
            carry = digits[i] / 10 >= 1
            digits[i] %= 10

        return [1] + digits if carry else digits
        

plusOne([1,2,3])