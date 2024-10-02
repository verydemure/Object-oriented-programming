class vechicle:


    #constrcutor Method(Funtion):
    def __init__(self, max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage



tesla = vechicle(180, 0)
lambo = vechicle(350, 3)


print("Tesla Max speed:", tesla.max_speed)
print("Tesla Max speed:", tesla.mileage)

print("Lambo Max speed:", lambo.max_speed)
print("lambo Max speed:", lambo.mileage)


