def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

# The function ordinary() got decorated and the returned function was given the name pretty.

def ordinary():
    print("I am ordinary")

ordinary()
make_pretty(ordinary)()