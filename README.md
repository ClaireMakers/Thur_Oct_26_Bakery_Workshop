# Bakery / Instantiating Objects from Classes

## Learning Objectives

In this workshop, you will learn to...

- Explain why classes are useful
- Instantiate classes
- Make two classes interact with each other

## Introduction

In this workshop, you are will practice instantiating classes and making them interact with one another. We will provide the class definitions.

> NOTE: You'll need to have your own local copy of the [Skills Workshops](https://github.com/makersacademy/skills-workshops) repo in order to do the exercises.

### Repeatable Execution

But first, consider this... Why do we bother with classes?

Let's go further... How about methods, functions and variables?

Each one is a tool that makes your life easier because each one allows you to write something once then use it repeatedly.

Variables allow you to declare a value once and then refer to it repeatedly...

``` python
variable_one = 10

variable_one += 15

variable_one *= 4
variable_one /= 50

print(variable_one)
```

Functions allow you to repeatedly execute some code...

``` python
def greeting(name):
    name = name.upper()
    name = name + "!!"
    print(f"Hello there, {name}!")

greeting("Will")
# => Hello there, WILL!!

greeting("Arthur")
# => Hello there, ARTHUR!!

greeting("Maggie")
# => Hello there, MAGGIE!!
```

Classes allow you to group functions / methods together with variables...

``` python
class Cake():
    def __init__(self):
        self.flavour = ""
        self.size = 100
    
    def set_flavour(self, flavour):
        self.flavour = flavour
    
    def take_slice(self, slice):
        self.size -= slice
        print(f"You have taken a {slice} sized slice. \n There is {self.size} percent cake remaining.")

gateau = Cake()
gateau.set_flavour = "Double Chocolate"
gateau.take_slice(40)

```

> NOTE: there is a difference between regular function calls `some_function(argument)` and instance method calls `new_obj.method_name(argument)`?

## Exercise 1 (10 mins)

In this first exercise, you will use our code to instantiate some cakes and a baker who can eat the cakes.

- **First**, have a quick look at the code in [bakery.py](./lib/bakery.py)
> NOTE: You'll need to be in the `bakery` directory for the next bit to work
- **Next**, open a Python REPL by doing `python3`, and then do `from lib.bakery import *` to load your classes
- **Now**, you're ready to instantiate some cakes and a baker (example below).

**Here's an example...**

``` python
    # Intended input/output in the Python REPL:
    
    # Instantiate a cake
    >>> cake = Cake()
    >>> cake
    <bakery.Cake object at 0x100f7d840>
    >>> cake.flavour
    ''

    # Give it a flavour
    >>> cake.set_flavour("Vanilla")
    >>> cake.flavour
    'Vanilla'

    # Instantiate a baker
    >>> will = Baker()
    >>> will
    <bakery.Baker object at 0x100f7d750>
    
    # Get your baker to eat some cake
    >>> will.eat_cake(cake, 20)
    You have taken a 20 percent sized slice.
    There is 80 percent cake remaining.
    >>> will.check_space()
    You have eaten 1 cakes.
    You have 80 percent space remaining in your belly!
    80
    
    # Make another cake and set give it a flavour
    >>> cake2 = Cake()
    >>> cake2.set_flavour("Strawberry")
    
    # Get your baker to eat more cake
    >>> will.eat_cake(cake2, 40)
    You have taken a 40 percent sized slice.
    There is 60 percent cake remaining.
    >>> will.check_space()
    You have eaten 2 cakes. 
    You have 40 percent space remaining in your belly!
    40
```

> The above is just an example. If you're not sure how to get started, use it as a guide in your REPL. Once you feel more confident, get creative and get more bakers eating more cakes.

### Extension

If you'd like a little extra challenge, try to...

- Write a loop which will create multiple cakes and add them to a list
- Write another loop which will make the baker sample each cake in the list if they have space in their belly

## Exercise 2

For exercise 2, you'll need [bakery_2.py](https://github.com/makersacademy/skills-workshops/blob/main/core_workshops/modern_software_engineering_foundation/1_basic_programming/bakery/lib/bakery_2.py)


To get started, load `bakery_2.py` in a Python REPL then opening a bakery and then follow the instructions...

```python
bakery = Bakery()
```

> If no instructions appear, please reach out to your coach.
