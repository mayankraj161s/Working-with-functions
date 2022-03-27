def n_root(x, n=2):
    """Returns: nth root of x"""
    return x**(1/n)

# __main__
x = float(input("Enter value of base x: "))
n = float(input("Enter value of n: "))
print("{}th root of x is".format(n),n_root(x, n))