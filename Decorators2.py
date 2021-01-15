# We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

'''is equivalent to
    def ordinary():
        print("I am ordinary")
    ordinary = make_pretty(ordinary)
'''

ordinary()

