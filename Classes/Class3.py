# Jonathan Klein
# 12/20/18
# Class3.py

import time

class Robot:
    population = 0
    robot_list = []


    def __init__(self, name):
        self.name = name
        self.battery_power = 100
        Robot.population += 1
        self.robot_num = Robot.population
        Robot.robot_list.append(self.name)
        print(f'Robot #{self.robot_num} successfully initiated.')
        time.sleep(0.5)


    def charge_robot(self):
        self.battery_power += 25
        if self.battery_power > 100:
            self.battery_power = 100
        print(f'Robot "{self.name}" has been charged up to 25%\n')


    def is_robot_alive(self):
        print(f'Unit "{self.name}" has {self.battery_power}% battery left.\n')


    def do_robot_things(self, action):
        if self.battery_power > 0:
            print((action + ' ')*10, end='\n')
            self.battery_power -= 10
            self.is_robot_alive()
        else:
            print(f'Insufficient battery level on unit "{self.name}"\n')


    @classmethod
    def robot_roll_call(cls):
        print('Robot Database:', end=' ')
        print(*Robot.robot_list, sep=', ')


unit1 = Robot('Jontron')
unit2 = Robot('Kentron')
unit3 = Robot('Camtron')
unit4 = Robot('Dentron')
unit5 = Robot('Jasontron')

