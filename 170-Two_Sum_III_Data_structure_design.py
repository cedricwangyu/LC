class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.data.append(number)
        return None
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        p = {}
        for num in self.data:
            if num in p:
                return True
            else:
                p[value - num] = 1
                
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)