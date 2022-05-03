class sumOfTwo:
    def __init__(self, inputlist, target) -> None:
        self.inputlist=inputlist
        self.target=target

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} is for finding index of values that add up"

    @property
    def inputlist(self):
        return self._inputlist
    @inputlist.setter
    def inputlist(self, inputlist):
        self._inputlist=inputlist

    @property
    def target(self):
        return self._target
    @target.setter
    def target(self, target):
        self._target=target

    def findIndex(self):
        for i in range(0, len(self.inputlist)):
            for j in range(i+1, len(self.inputlist)):
                if(self.inputlist[i]+self.inputlist[j] == self.target):
                    return (i,j)
                
