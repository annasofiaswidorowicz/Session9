def greet():
    """
    Prints a basic greeting
    :return: None
    """
print("Hello, what a lovely day!")
print("I love walking in the park")

def greet_name(name):
    """
    Prints a basic greeting to a certain person
    :param name: the name of the person to greet
    :return: None
    """
    print(f"Hello {name}, nice to meet you!")

def average(a, b):
    """
    Calculates the average of a and b
    :param a: first number
    :param b: second number
    :return: None
    """
    print(f"The average of {a} and {b} is {(a + b) / 2}")

def average2(a, b):
    """
    Calculates the average of a and b
    :param a: first number
    :param b: second number
    :return: returns a float, the average result
    """
    return(a + b) / 2

def average_multiple(a, b, c=0):
    """
    Calculates the average of 2 or 2 numbers
    :param a:
    :param b:
    :param c:
    :return: the average of 2 or 3 numbers
    """
    if c ==0:
        return(a + b) / 2
    else:
        return(a + b + c) / 3

#to see something, we need to "call" the function
for i in range(10):
    greet()

greet_name("Bob")
greet_name("Jessica")
average(10, 20)
average(20, 30)
n1 = average2(20, 40)
n2 = average2(40, 50)
print(f"I calculated 2 averages: {n1}, {n2}")
average_2 = average_multiple(10, 20)
average_3 = average_multiple(10, 20, 90)
print(f"I calculated 2 averages: {average_2, average_3}")











