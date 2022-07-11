#primer number
import math
import random
#I have not finished

def is_prime(p):
    for n1 in range(2, math.isqrt(p)):
        if p%n1 == 0:
            return False
    else:
        return True

def get_prime(size):
    while True:
        p= random.randrange(size,2*size)
        if is_prime(p):
            return p

print(get_prime(100000))