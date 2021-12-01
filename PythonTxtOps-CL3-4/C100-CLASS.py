class Car(object):
    def __init__(self, speed, model, brand, price):
        self.speed = speed
        self.model = model
        self.brand = brand
        self.price = price
        print("Model Is : " + self.model + " Speed Is : " + self.speed + " Brand Is : " + self.brand + " Price Is : " + self.price)
    def start(self, speed, model, brand, price):
        print("Car Started" + "Model Is : " + self.speed + "Model Is : " + self.model + "Brand Is : " + self.brand + "Speed Is : " + self.price)
    def stop(self):
        print("Car Stopped")
        
SilentShadow = Car("280kmph", "SilentShadow", "RollsRoyace", "$455,000")
print(SilentShadow.__init__(SilentShadow.speed, SilentShadow.model, SilentShadow.brand, SilentShadow.price))