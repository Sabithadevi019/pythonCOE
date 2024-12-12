basic=int(input("Enter the salary"))
if(basic<10000):
    hra=(67/100)*basic
    da=(73/100)*basic
elif(10000<basic<20000):
    hra=(69/100)*basic
    da=(76/100)*basic
else:
    hra=(73/100)*basic
    da=(89/100)*basic
gross=hra+da+basic
print("Gross", gross)