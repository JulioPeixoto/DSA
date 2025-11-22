class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.park[carType - 1] -= 1
        if self.park[carType - 1] < 0:
            return False
        return True