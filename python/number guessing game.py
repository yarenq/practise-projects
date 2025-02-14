import random

min_number=1
max_number=100

number=random.randint(min_number,max_number)
guess=int(input("enter a number"))
guess_count=1

while number!=guess :
    if guess<number:
        print("up")
    else:
        print("down")
    guess=int(input("try again,enter a number"))
    guess_count+=1

print("congratulations")
print(f"guess count:{guess_count}")