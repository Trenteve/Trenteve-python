float age = 18.5

len(list) lists the length of a list, dictionary, set, tuple, etc.

4 // 2 = floor division - does the division then rounds down

boolean operators are: 'and', 'or', and 'not'
    If an or operator is used it doesn't return the first value if it is false, it returns the second value.

Ternary operator: 
    def is_adult(age)
        return True if age > 18 else return false

Turning a string into a number: str(39)

A multi-line string: 
    print(""" This

        Is a 

        multi line string.
    """)

If name was a string name[-1] would return the last letter of that string.
    substring or split: name[1:3]
    Works with lists as well.

Boolean functions: any([value1], [value2]) returns true if any of the values are true. all()

Complex numbers: 'imaginary' numbers using 'j' to signal an imaginary number.
    num = 1 + 2j
    num2 = complex(1, 2)
round(5.49, 1) - rounds to the tenth value

ENUMs: Creates constant values, use .value to get the value of the constant
    from enum import ENUM

    class State(enum):
        INACTIVE = 0
        ACTIVE = 1

    print(State['ACTIVE']) #returns 1
    print(list (State)) #returns all values in State

Add an item to a list: append('item')
Combine two lists: extend([item1], [item2]) or += ([item1], [item2])
Remove an item: remove(item2)
Insert an item: insert(2, item1)
Sorts the list w/o caring about uppercase or lowercase: .sort(key=str.lower)
    changes the list.
    To not change the list: sorted(list, key=str.lower)

Tuples: defines a collection of constants(not modifiable) 
    items(item1, item2) #notice the parentheses

Dictionaries: Use curly braces and name : value pairs.
    dict.get(key, "default_value") - gets the value pair from the key or returns the second value.
    .pop() removes the last item and returns it
    .popitem() removes the last key : value pair and returns it
    dict((dict.items or dict.keys. or dict.values)) returns whatever you chose from the dictionary.
    add a key value pair to the dict: dict["key"] = ["value"]
    deleting a key value pair: del dict["key"]
    Copying a dictionary: dictCopy = dict.copy()

Sets: Primary use them for mathematical purposes, uses curly braces, cannot have two of the same item in a set
    set1 = {"Roger", "Syd"}
    set2 = {"Roger"}
    mod = set1 & set2 #returns 'Roger'  intersect
    mod = set 1 | set2 #returns 'Syd', 'Roger'  union
    mod = set1 - set2 #returns 'Syd'    difference
    mod = set1 > set2 #returns True     Does set1 have everything set2 has?

Functions:
    To set a default value of a function: def hello(name='my friend')
        So if hello() is called with no argument it will return my friend

Nested Functions:
    Declaring a variable with nonlocal lets you access variables from the outer function in the inner function.

For loop: 
    for item in list:
    for item in range(15): #return a list that goes from 0-14
    for index, item in enumerate(list):
        print(index, item) #returns a the index of each item and each item
    break stops the loop altogether, continue stops the current iteration of the loop and has it go onto the next one.

Inheritance:
    For a class Dog inheriting class Animal:
        class Dog(Animal):
    Instead of importing an entire file you can:
        from file import function
        subfolder: from lib.file import function
    If you want to import a folder in a sub folder: You have to make a file labelled __init__.py.
    
Accepting arguments in the command line:
    Importing sys or argparse.
    parser = argparse.ArgumentParser();
    parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red', 'yellow}, help='the color to search for') #checks if the color the user inputs is first of all a color and if it is red or yellow.
    args = parser.parse_args()

Lambda functions:
    multiply = lambda a, b : a * b
    print(multiply(2, 4)) #returns 8

Map(): whenever you want to run a function on every item on a list.
    map(function, list) or if able to simplify use a lambda function; map(lambda a : a * 2, list)

Filter(): Want to create another iterable with changes to the list.
    filter(function, list) #the function usually returns true or false

Reduce(): When you want to apply a function to an iterable and reduce it to a single cumulative value.
    Has to import it: from functools import reduce
    reduce(lambda a, b : a[1] + b[1], list)

Decorators: Use decorators to do something before and after a function. Called using an @decorator_name. Use when you want to change a functions functionality without actually changing the function.
    def logtime(func):
        def wrapper():
            #do something before
            val = func()
            #do something after
            return val
        return wrapper

To put a docString in a file """...""" the purpose is to explain the functionality of the file.

Annotations are used to specify what type a variable will be, what type of input a function should take. Helpful for large pieces of code.
    ex. count: int = 0 #python will ignore these annotations

Exception handling
    try:
        except <ERROR1>:
            #handler
        except <ERROR2>:
            #handler
    else:
    finally:

    Raising an exception:
        try:
            raise Exception(An Error!)
        except Exception as error:
            print(error)

    Creating an Exception class:
        class FileNotFoundException(Exception):
            pass #has to be used when a class is made with no methods

Inputting files using with: automatically closes the file
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

Installing and uninstalling packages using pip, done in the terminal.
    All packages are on pypi.org
    pip install -U package_name #-U installs the latest version.

List Compression
    numbers_power_2 = [n**2 for n in numbers] #numbers is a list and this list compression does the job of a loop by taking every number in that list and squaring it.

Creating a constructor
    def __init__(self, name, age):

Operator overloading
    Creating a function that responds to a certain operator like +, *, -, etc.
    def __add__(self, other):
        return self.age + other.age
    print(self + other)
        This add method would be in the class with a constructor that initializes the ages.

In a class in order to access a variable in multiple functions, we must use self.variable.