#https://leetcode.com/problems/palindrome-number/
class Palindrome:
    def __init__(self, inputNum) -> None:
        self.inputNum = inputNum
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} created to find palindrome numbers"

    @property
    def inputNum(self):
        return self._inputNum

    @inputNum.setter
    def inputNum(self, inputNum):
        self._inputNum = inputNum

    def checkPalindrome(self):
        if(self.inputNum < 11):
            return False
        else:
            print(self.inputNum)
            orginputvalue=f"{self.inputNum}" 
            reverseValue=orginputvalue[::-1]
            if(orginputvalue == reverseValue):
                return True
            else:
                return False
        
