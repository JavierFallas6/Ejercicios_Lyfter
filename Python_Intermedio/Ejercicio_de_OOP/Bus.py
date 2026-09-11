class Bus:
    bus_passengers = []
    def __init__(self,max_passengers):
        self.max_passengers = max_passengers

    def get_in(self,person):
        if len(self.bus_passengers)< self.max_passengers:
            self.bus_passengers.append(person)
            print(self.bus_passengers)
        else: 
            print("The bus is out of seats")

    def get_off(self,person):
        for index, record in enumerate(self.bus_passengers):
            if record == person:
                self.bus_passengers.pop(index)

        print(f"{person} got off the bus")

bus_1 = Bus(2)
bus_1.get_in("Juan")
bus_1.get_in("pedro")
bus_1.get_in("luis")
bus_1.get_off("Juan")

