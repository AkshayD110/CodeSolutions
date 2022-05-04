
from fcntl import F_SEAL_SEAL


class monotonicArray:
    def __init__(self, nums) -> None:
        self.nums=nums

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} is a monotonic Array finder class"

    @property
    def nums(self):
        return self._nums

    @nums.setter
    def nums(self, nums):
        self._nums=nums

    def isMonotonic(self):
        lenght_of_array=len(self.nums)
        output=0
        if(len(self.nums==1)): return True
        if(self.nums[0]<self.nums[lenght_of_array-1]):
            for i in range(1, len(self.nums)):
                if(self.nums[i-1] <= self.nums[i]):
                    output=1
                else:
                    output=0
                    return False
        else:
            for i in range(1, lenght_of_array):
                if(self.nums[i-1]>=self.nums[i]):
                    output=1
                else: 
                    output=0
                    return False
        if(output==0):
            return False
        else: return True

    def betterMonotonic(self):
        nums=self.nums
        value=(all(nums[i]<nums[i+1] for i in range(len(nums)-1)) or 
        all(nums[i]>nums[i+1] for i in range(0, len(nums)-1)))
        print(value)
