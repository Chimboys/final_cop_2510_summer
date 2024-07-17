# Single Inheritance Example
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        Animal.make_sound(self)
        print("Bark")

# Example usage
dog = Dog()
dog.make_sound() 

## Multiple Inheritance Example
class Parent1:
    def show(self):
        print("Message from Parent1")
        super().show()

class Parent2:
    def show(self):
        print("Message from Parent2")
        

class Child(Parent1, Parent2): #the important is important
    def show(self):
        print("Message from Child")
        super().show()  # Calls Parent1's show() method, and Parent1 calls Parent2's show() method
       
       

# Example usages
child = Child()
child.show()

