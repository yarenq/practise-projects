product_name=input("enter the products name")
last_months_price=float(input("enter last months price"))
this_months_price=float(input("enter this months price"))
change=this_months_price-last_months_price
percentage_of_change=change/last_months_price*100
print("change of the products price=",change)
print("percentage of the change=",percentage_of_change,"%")
