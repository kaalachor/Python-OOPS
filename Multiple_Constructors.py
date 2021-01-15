# when multiple constructors are used, the last one is called.

class Student:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second contructor")  
    
st = Student()  