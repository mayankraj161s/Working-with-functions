def volume(l,b,h):
    """Returns: Volume of a cuboid"""
    return l*b*h

# __main__
print("VOLUME CALCULATOR")
print("-------------------")
print("Note: All data should be in metres.")

# Taking parameters
length = float(input("Enter length: "))
width = float(input("Enter width: "))
height = float(input("Enter height: "))

vol = volume(length,width,height)

print("The volume of the box is",vol,"m\u00b2")