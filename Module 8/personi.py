class Personi:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        print(f"Hello, I am {self.name}, and I am {self.age} years old")


person1 = Personi("Alice",15)
person2 = Personi("Bob",17)

person1.greet()
person2.greet()


