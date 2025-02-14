number=int(input("enter a number: "))
root=int(number**0.5)
while number>1:
    for i in range(2,root+1):
        if number%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")
    number=int(input("enter a number"))






