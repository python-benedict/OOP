#   Take input from a User (name, Age, Marks)
#   create a class with __init__ method and also create an action method display to display the attributes
#   Also try to use argument and parameter with different objects


class Student():
    def __init__(self, n, a, **m):
        self.name =n
        self.age = a
        self.mark =m

    def display(self):
        print('hi - ', self.name)
        print('Your age - ', self.age)
        print('Your mark - ', self.mark)

s1 = Student('Benedict', 23,biology = 78, physics =34, chemistry = 87)
s1.display()