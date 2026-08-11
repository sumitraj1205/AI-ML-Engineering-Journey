b = int(input("enter a no."))
if b < 30000:
    tax = (b*5)/100
elif  30000 < b < 70000:
    tax = (b*15)/100
else:
    tax = (b*25)/100
print("total tax =",tax)