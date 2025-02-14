fx=0
count=0
total=0

for x in range(-3,4):
    for y in range(-3,4):
        if x!=-y:
            fx=(2*x+3*y-4*x*y+5)/(x+y)
            count+=1
            total+=fx




print(f"average: {total/count:.2f}")
