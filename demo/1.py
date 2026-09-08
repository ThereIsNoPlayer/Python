age=int(input("enter your age"))
if age<4:
    price=0
elif age>=4 and age<=17:
    price=5
elif age>17 and age<=64:
    price=10
else:
    price=5
print("price is",price)