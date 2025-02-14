name1=input("enter the name of the first team")
name2=input("enter the name of the second team")
sets_won1=int(input("enter the number of sets won by the first team"))
sets_won2=int(input("enter the number of the sets won by the second team"))

if sets_won1==3 and sets_won2==0 or sets_won1==3 and sets_won2==1 :
    print(f"The name of the team that won the match:{name1}, points earned:3")
    print(f"The name of the team that lost the match:{name2}, points earned:0")
if sets_won1==0 and sets_won2==3 or sets_won1==1 and sets_won2==3 :
    print(f"The name of the team that won the match:{name2}, points earned:3")
    print(f"The name of the team that lost the match:{name1}, points earned:0")

if sets_won1==3 and sets_won2==2 :
    print(f"The name of the team that won the match:{name1}, points earned:2")
    print(f"The name of the team that lost the match:{name2}, points earned:1")
if sets_won1 == 2 and sets_won2 == 3:
    print(f"The name of the team that won the match:{name2}, points earned:2")
    print(f"The name of the team that lost the match:{name1}, points earned:1")







