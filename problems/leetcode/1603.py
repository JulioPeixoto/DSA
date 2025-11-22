class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]
        print(self.parking)

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.parking[0] > 0:
                self.parking[0] -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.parking[1] > 0:
                self.parking[1] -= 1
                return True
            else:
                return False
        if carType == 3:
            if self.parking[2] > 0:
                self.parking[2] -= 1
                return True
            else:
                return False


# ============= TESTES =============

# Teste 1: Exemplo do problema
print("Teste 1: [1, 1, 0]")
parking = ParkingSystem(1, 1, 0)
assert parking.addCar(1) == True  # big car - tem vaga
assert parking.addCar(2) == True  # medium car - tem vaga
assert parking.addCar(3) == False  # small car - não tem vaga
assert parking.addCar(1) == False  # big car - já ocupado
print("✓ Teste 1 passou\n")

# Teste 2: Múltiplas vagas
print("Teste 2: [3, 2, 1]")
parking = ParkingSystem(3, 2, 1)
assert parking.addCar(1) == True  # big: 3 -> 2
assert parking.addCar(1) == True  # big: 2 -> 1
assert parking.addCar(2) == True  # medium: 2 -> 1
assert parking.addCar(1) == True  # big: 1 -> 0
assert parking.addCar(1) == False  # big: 0 (sem vaga)
assert parking.addCar(2) == True  # medium: 1 -> 0
assert parking.addCar(2) == False  # medium: 0 (sem vaga)
assert parking.addCar(3) == True  # small: 1 -> 0
assert parking.addCar(3) == False  # small: 0 (sem vaga)
print("✓ Teste 2 passou\n")
