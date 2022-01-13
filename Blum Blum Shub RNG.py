# The Blum Blum Shub (BBS) PRNG
# Created with help from:
# Author: William Stallings
# Date: 2017
# Title: Blum Blum Shub RNG
# Availability: Cryptography and Network Security Principals and Practice Seventh Edition (Pearson Education)
# Pages: 242-243, 711-712

from sympy import randprime
from tabulate import tabulate


class BBS_PRNG():

    def __init__(self):
        self.bitlen = int(input("Enter the bit length (The length of the prime factors): "))
        self.seed = int(input("Enter the seed (Initial value to start): "))
        self.numbits = int(input("Enter the number of bits (iterations): "))

    def bbs_init(self):

        # Generates two random prime numbers (p, q) that either have a remainder of 3 when divided by 4
        # or are greater than 2 ^ (bit length - 1)
        p = 3
        while (p < 2 ** (self.bitlen - 1)) or (3 != (p % 4)):
            p = randprime(2, 2 ** self.bitlen)

        q = 3
        while (q < 2 ** (self.bitlen - 1)) or (3 != (q % 4)):
            q = randprime(2, 2 ** self.bitlen)

        n = p * q
        x = self.seed ** 2 % n

        # The internal state that will be used to get the random numbers
        state = [n, x]
        return state

    def bbs_gen(self):

        full_list =[]
        ranbits = []

        state = self.bbs_init()

        n = state[0]
        x = state[1]

        # Adds the headers to the list and the first entry to the list
        full_list.append(['i', 'Xi', 'Bi'])
        full_list.append([0, x, None])

        # Iterates num bits times to get the random numbers
        for i in range(1, self.numbits + 1):
            x = x ** 2 % n
            b = x % 2
            ranbits.append(b)
            full_list.append([i, x, b])

            # Updates the state
            state[1] = x

        #Returns the output in for the generation of the random bits and the random bits in a dictionary
        return {'full': full_list, 'rbits': ranbits}


bbs = BBS_PRNG()
bbs_bits = bbs.bbs_gen()
print(bbs_bits['rbits'])
print(tabulate(bbs_bits['full'], headers='firstrow', tablefmt='fancy_grid'))
