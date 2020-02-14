# Jonathan Klein
# 12/18/18
# Class2.py

class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.gas_miles = 500
        self.gas = 10

    def honk(self):
        print('Honk! Honk!\n')

    def drive(self, milesDriven):
        gas_used = milesDriven/50
        maxMiles = self.gas*50
        if gas_used <= self.gas:
            self.gas_miles += milesDriven
            self.gas -= gas_used
            print(f'You\'ve driven {milesDriven} miles and used {gas_used} gallons of gas!\n')
        elif gas_used > self.gas:
            print(f'You attempted to drive {milesDriven} but only made it {maxMiles} miles in.\nYou had {milesDriven-maxMiles} miles remaining.\n')
            self.gas_miles += milesDriven
            self.gas -= maxMiles/50
        else:
            print('Invalid input. Please input a positive integer.\n')

    def gasFillUp(self, gas):
        self.gas += gas

    def registration(self):
        print(f'''
Year: {self.year}
Make: {self.make}
Model: {self.model}
Miles: {self.gas_miles}
Gas: {self.gas}
    ''')

car1 = Car(2018, 'Toyota', 'Camry')
car2 = Car(2019, 'Honda', 'Accord')
car3 = Car(2019, 'Chevrolet', 'Traverse')

print(f'{car2.gas_miles} miles\n{car2.gas} gallons of gas\n')
car2.drive(531)
print(f'{car2.gas_miles} miles\n{car2.gas} gallons of gas\n')

