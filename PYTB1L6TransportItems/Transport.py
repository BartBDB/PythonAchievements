import time
import os

def printLists():
    os.system("cls")
    print("factory: " + str(factory))
    print("distribution: " + str(distribution))
    print("shop: " + str(shop))
    time.sleep(1)

factory = ["Stoel"]
distribution = []
shop = []

printLists()

distribution.insert(0, "Stoel")
factory.clear()

printLists()

shop.insert(0, "Stoel")
distribution.clear()

printLists()