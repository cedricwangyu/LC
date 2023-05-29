class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.limits = [big, medium, small]
        self.p = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
        if self.p[carType-1] < self.limits[carType-1]: 
            self.p[carType-1] += 1 
            return True
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)