from random import randrange

def randoms(n):
    """Returns: n-digit number"""
    if n < 1:
        a = "Incorrect input"
    else:
        a = randrange(10**(n-1),10**n)
    return a

# __main__
n = int(input("Enter n: "))
print("Random {}-digit number is".format(n),randoms(n))