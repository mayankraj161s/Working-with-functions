from random import randint

def randoms(a, b):
    """Returns: Random number within two limits"""
    return randint(a,b)

# __main__
l_lim = int(input("Enter lower limit: "))
u_lim = int(input("Enter upper limit: "))

for i in range(3):
    r = randoms(l_lim, u_lim)
    print("Number {}:".format(i+1),r)