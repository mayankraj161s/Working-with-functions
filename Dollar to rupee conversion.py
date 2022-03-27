def dollar_to_rupee(dollar,conv_price):
    '''It will convert dollar into rupees.'''
    rupee = dollar * conv_price
    return rupee

def dollar_to_rupee1(dollar,conv_price):
    '''It will convert dollar into rupees.'''
    rupee = dollar * conv_price
    print("Corressponding amount in rupees: ₹",rupee)

amount = float(input("Enter amount in dollars: $ "))
conversion_price = float(input("Enter conversion price: "))
print("Using void function 👇")
a = dollar_to_rupee(amount, conversion_price)
print("Corressponding amount in rupees: ₹",a)
print("-"*45)
print("Using non-void function 👇")
dollar_to_rupee1(amount, conversion_price)

print("Press any key to Quit: ",end='')
a = input()
quit()