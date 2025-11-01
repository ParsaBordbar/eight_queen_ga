import random

def swap(item1, item2):
    item1 = item1 ^ item2
    item2 = item1 ^ item2
    item1 = item1 ^ item2
    return item1, item2

def select_a_random():
    index = random.randint(0, 7)
    return index