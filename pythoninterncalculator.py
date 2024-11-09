m=int(input("enter a number"))
n=int(input("enter another number"))
op=input("enter your choice of operation")
if op=="addition":
    print(m+n)
elif op=="subtraction":
    print(m-n)
elif op=="multiplication":
    print(m*n)
elif op=="division":
    print(m/n)
elif op=="floor division":
    print(m//n)
elif op=="remainder":
    print(m%n)
elif op=="exponentiation":
    print(m**n)
print("the calculated value is: ",op)
    


