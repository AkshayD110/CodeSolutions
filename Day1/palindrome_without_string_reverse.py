import math
class palindrome_without_stringreverse:
    def __init__(self, inputNum) -> None:
        self.inputNum = inputNum

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} is the class for knowing if a number is palindrome"

    @property
    def inputNum(self):
        return self._inputNum

    @inputNum.setter
    def inputNum(self, inputNum):
        self._inputNum=inputNum

    def isPalindrome(self):
        if(self.inputNum < 11):
            return False
        else:
            inputvalue=self.inputNum
            input_digits=len(str(self.inputNum))
            rev_value=0
            x=0
            for i in range(input_digits, 0, -1):
                temp=pow(10, x)
                num=pow(10, input_digits-1)
                (quo, rem)=divmod(inputvalue, num)
                inputvalue=rem
                rev_value=rev_value+(quo*temp)
                input_digits = input_digits-1
                x=x+1

            print(f"Original value is {self.inputNum}")
            print(f"Reveresed value is {rev_value}")
            if(self.inputNum==rev_value):
                return True
            else:
                return False