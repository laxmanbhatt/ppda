n=int(input("Enter a number: "))
t=n
rev=0
while n!=0:
    print("The value of n is: ", n)
    r=n%10
    print("The value of r is: ", r)
    rev=rev*10+r
    print("The value of rev is: ", rev)
    n=n//10
    print("The value of n is: ", n)
print("reverse of number", t, "is: ", rev)
