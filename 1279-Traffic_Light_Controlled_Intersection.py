class TrafficLight:
    def __init__(self):
        self.curr = True

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        if (direction < 3 and not self.curr) or (direction > 2 and self.curr): 
            turnGreen()
            self.curr = not self.curr
        crossCar()
                
        