number_of_days=int(input("enter today's number"))
rainy_day=0
rain_amount=0

for day in range(1,number_of_days):
    print(day)
    day+=1
    rain=float(input("enter the amount of rain"))
    rain_amount+=rain
    if rain>0 :
        rainy_day+=1

percentage=rainy_day/number_of_days*100
average_rain= rain_amount/number_of_days

print(f"""number of rainy days:{rainy_day},
percentage of rainy days:{percentage},
average amount of rain per day:{average_rain}""")

