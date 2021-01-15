from abc import ABC,abstractmethod

class abs(ABC):
    @abstractmethod
    def sides(self):
        pass

class triangle(abs):
    def sides(self):
        print('I have three sides')

t = triangle()
t.sides()

# trying to instantiate abstract classes
try:
    a = abs()
    a.sides()
except Exception as e: print(e)
    