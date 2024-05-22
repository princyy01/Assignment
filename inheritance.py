class Father:
    def __init__(self, father_name, father_age):
        self.father_name = father_name
        self.father_age = father_age
        
    def father_hii(self):
        print("Father's name is:", self.father_name)
        print("And his age is:", self.father_age)
        
class Son(Father):
    def __init__(self, father_name, father_age, son_name, son_age):
        super().__init__(father_name, father_age) # super keyword is used to call any parent class method, here used to call parent class constructor
        self.son_name = son_name
        self.son_age = son_age
    
    def son_hii(self):
        print("My name is:", self.son_name)
        print("And my age is:", self.son_age)

son_instance = Son("Ramesh Sharma", 75, "Mohit Sharma", 50)

son_instance.father_hii()
son_instance.son_hii()
