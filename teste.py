class person:

    def __init__(self,a,b):
        self.__name="None"
        self.__age=0

        self.set_name(a)
        self.set_age(b)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self,a):
        if a.isalpha() or ' ' in a:
            self.__name = a

    def set_age(self,a):
        if a>0 and a<120:
            self.__age = a

    def __str__(self):
        return '\nName : {}\nAge : {}'.format(self.get_name(),self.get_age())


class student(person):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.__sid = c

    def get_sid(self):
        return self.__sid

    def __str__(self):
        return '{} \nSID : {}'.format(super().__str__(),self.get_sid())



p1 = person('Jean Mi',11)

print(p1)



s1 = student('Bob',12,13)
s2 = student('Bo',11,12)
s3 = student('B',10,11)

print(s1)


list_of_objects=[s1,s2,s3]


y = 0
while y == 0:
    name = input("\nType the name : ")
    age = int(input("\nType the age : "))
    sid = input("\nType the SID : ")

    list_of_objects.append(student(name,age,sid))

    cont = input("\nContinue ? (y/n) : ")
    if 'n' in cont:
        y = 1


print('\n============LIST PRINTING=============')

for i in list_of_objects:

    print(i)
    print('\n======================================')