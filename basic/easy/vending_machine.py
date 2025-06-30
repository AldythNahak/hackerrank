#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    def __init__(self, num_items, item_coins):
        self.stock = num_items
        self.price = item_coins

    def buy(self, num_items, num_coins):
        total = num_items * self.price

        if num_items > self.stock:
            raise ValueError("Not enough items in the machine")

        if num_coins < total:
            raise ValueError("Not enough coins")

        self.stock -= num_items
        return num_coins - total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
