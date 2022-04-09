class Car(object):
     #underscore
    def __init__(self,model,colour,company):
        self.model=model
        self.colour=colour
        self.company=company
        
    def start(self):
        print("the car started")
        
    def stop(self):
        print("the car stopped")

car1 = Car("A6","red","audi")
car1.start()
print(car1.colour)