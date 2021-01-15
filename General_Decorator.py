# This decorator can decorate any function 
# args will be the tuple of positional arguments.
# kwargs will be the dictionary of keyword arguments.

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

@works_for_all
def demo():
    print('demo')

demo()