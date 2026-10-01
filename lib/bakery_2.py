from random import random as rand
from time import sleep

class Cake():
    def __init__(self):
        self.flavour = ""
        self.size = 100
    
    def set_flavour(self, flavour):
        self.flavour = flavour
    
    def take_slice(self, slice):
        self.size -= slice
        print(f"You have taken a {slice} percent sized slice. \n There is {self.size} percent cake remaining.")


class Bakery():
    MAX_ORDERS = 5

    def __init__(self):
        self.completed = 0
        self.order = {}
        sleep(2)
        self.create_new_order()


    def flavour_rand(self):
        rand_perc = round(rand() * 100)
        if rand_perc > 80:
            return "Strawberry"
        elif rand_perc > 60:
            return "Vanilla"
        elif rand_perc > 40:
            return "Chocolate"
        elif rand_perc > 20:
            return "Banana"
        else:
            return "Carrot"

    def satisfy_order(self, cake):
        if cake.flavour != self.order["flavour"]:
            print(f'The flavour is incorrect! The customer asked for {self.order["flavour"]}, not {cake.flavour}!')
            return
        else:
            print("The flavour is correct!")
            sleep(1)

        if cake.size != self.order["size"]:
            print(f'The size is incorrect! The customer asked for {self.order["size"]}, not {cake.size}!')
            return
        else:
            print("The size is correct!")
            sleep(1)
        
        
        print("Order Satisfied!")
        sleep(1)
        self.completed += 1

        if self.completed >= self.MAX_ORDERS:
            print("Congratulations! That's all the orders completed! Well done!")
            exit()
        else:
            print(f"That's {self.completed} orders down! {self.MAX_ORDERS - self.completed} to go. Keep going!")
            sleep(1)
            self.create_new_order()

    def create_new_order(self):
        flavour = self.flavour_rand()
        size = round(rand() * 100)
        self.order["flavour"] = flavour
        self.order["size"] = size
        print(f"A new order has just come in! The customer wants a {flavour} flavour cake that is {size} big!")
        sleep(1)
