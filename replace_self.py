# This is to show that the normal 'self' keyword we use in python classes can be changed
#provided we stay consistent

class Student:
    def __init__(ppo, n,a,m):
        ppo.name = n
        ppo.age = a
        ppo.mark = m

    def display(ppo):
        print('My age is ', ppo.name)
        print('My age is: ', ppo.age)
        print('My mark is ', ppo.mark)

s1 = Student('Osei Sefa', 34,56)
s1.display()