# Exercise
# create a class for a vehicle that has 3 variables (door, speed and make-model)
# create constructor __init__, getters and setters
# create function named accelerate to increase speed by 10
# create function named break to reset the speed to zero
# str to print the values of the variables
# create multiple objects will different values

class vehicle:
    def __init__(self,x,y,z):
        self.__doors = x
        self.__speed = y
        self.__makeModel = z


    def get_Doors(self):
        return self.__doors

    def get_Speed(self):
        return self.__speed

    def get_makeModel(self):
        return self.__makeModel


    def set_Doors(self,a):
        if a > 0 and a <= 5:
            self.__doors = a
        else:
            print("Select between 1 and 5")


    def set_Speed(self,a):
        if a > 0 and a <= 120:
            self.__speed = a
        else:
            print("Select between 1 and 120")

    def set_makeModel(self,a):
        if a.isalpha():
            self.__makeModel = a
        else:
            print("Characters Only")




    def accelerate(self):
        self.__speed = self.__speed + 10

    def speedBreak(self):
        self.__speed = 0


    def __str__(self):
        return '\nDoors : {} \nSpeed : {} \nMake-Model : {} '.format(self.get_Doors(),self.get_Speed(),self.get_makeModel())




test1=vehicle(1,2,'Toyota Corola')

test1.set_Doors(5)

print(test1)



