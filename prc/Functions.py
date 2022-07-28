# Functions with parameters
def display(a, b, c):
    print(a)
    print(b)
    print(c)


# We need to follow the order in default method
display("Hello", "Ji", "Kya Haal")

# Another way and in this we don't need the order as we specify the variable with argument
display(b="Ji", c="Kya Haal", a="Hello")


# Writing a documentation for a function which is visible when hovered over it
def doc():
    """This is documentation of doc function"""
    print("You can see that where you called this function !")


doc()


def outer():
    def inner():
        print("In inner")

    inner()
    print("Outer")


outer()

# We can store a function in a variable like this
x = outer
x()
