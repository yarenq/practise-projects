gross_salary =1
worker = -1 #number of workers

#defining the valuables for gross salary levels
low = 0
medium = 0
high = 0
really_high = 0 #amount of sales representatives with a gross salary of more than $50000
#defining the valuables for totals
total_net_salary = 0
total_gross_salary = 0
total_tax = 0

tax_rate = 0
while gross_salary > 0:
    gross_salary = int(input("Please enter your gross salary: "))
    worker += 1
    if 0 < gross_salary <= 10000:
        low += 1
        tax_rate = 0.15
    elif 10000 < gross_salary <= 25000:
        medium += 1
        tax_rate = 0.2
    elif 25000 < gross_salary < 50000:
        high += 1
        tax_rate = 0.25
    elif gross_salary > 50000:
        really_high += 1
        tax_rate = 0.25

    tax = gross_salary * tax_rate
    net_salary = gross_salary - tax

    # as the loop works, it adds the new values to the total amount
    total_net_salary += net_salary
    total_gross_salary += gross_salary
    total_tax += tax

    if gross_salary > 0:
        print(f"""The amount of income tax to be paid to the state:{tax}$
Net salary to be paid to the sales representative:{gross_salary-tax}$""")

print(f"""Number of sales representatives with low salaries:{low}
Number of sales representatives with medium salaries:{medium}
Number of sales representatives with high salaries:{high}""")

print(f"""Percentage of sales representatives with a gross salary of more than $50000 among sales representatives with a high gross salary level:{really_high/(really_high+high)*100:.2f}""")

print(f"Average of all sales representatives' net salary:{total_net_salary/worker:.2f}$")

print(f"""The total amount of income tax to be paid to the state:{total_tax}$, 
and the percentage of this amount in the total gross salary:{total_tax/total_gross_salary*100:.2f}%""")
