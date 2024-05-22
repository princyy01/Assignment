""" A static method is a method that belongs to the class rather than to any specific instance of the class. 
This means you can call a static method without creating an object of the class. 
Static methods can be used to perform operations that are not dependent on the instance of the class."""
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

result_add = MathOperations.add(5, 3)
result_multiply = MathOperations.multiply(5, 3)

print(f"Addition: {result_add}")       
print(f"Multiplication: {result_multiply}")  
