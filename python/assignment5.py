matches=int(input("enter the number of matches: "))
points_won=0
points_lost=0
long_match=0 #number of matches finished in 5 sets
matches_won=0
perfect_match=0 #matches without losing any sets
max_difference=0 #not really sure about this one
all_total_points_won=0 #total points won in all the matches
all_total_points_lost=0

for count in range(1,matches+1): #loops for every match
    team_name=input("Enter the name of the opposing team: ")
    sets_won = 0
    sets_lost = 0
    total_points_won=0
    total_points_lost=0
    for sets in range(1,6): #loops for every set
        if sets_won<3 :
            points_won=int(input(f"Enter the number of points won for {sets}. set: "))
            points_lost=int(input(f"Enter the number of points lost for {sets}. set: "))
            print("")
            total_points_won += points_won
            total_points_lost += points_lost
            if points_won>points_lost:
                sets_won+=1
            elif points_won<points_lost:
                sets_lost+=1
        elif sets_won==3:
            matches_won+=1
            if sets_lost==0:
                perfect_match+=1
        if sets_won+sets_lost==5:
            long_match+=1

        if sets_lost==3 or sets_won==3:
            break



    all_total_points_won += total_points_won
    all_total_points_lost += total_points_lost

    print(f"""ABOUT THIS MATCH
    Total number of points won:{total_points_won}
    Total number of points lost:{total_points_lost}
    Total number of sets won:{sets_won}
    Total number of sets lost:{sets_lost}
    Average of points won per set:{total_points_won / (sets_won + sets_lost):.2f}
    Average of points lost per set:{total_points_lost / (sets_won + sets_lost):.2f}""")

    difference = total_points_won - total_points_lost  # the difference between the total points won and the total points lost in the match

    if difference>max_difference: #finding the team with the highest point difference
        max_difference=difference
        highest_team=team_name

print("")
print(f"""ABOUT ALL THE MATCHES PLAYED
Total number of points won:{all_total_points_won}
Average of points won per match:{all_total_points_won/matches:.2f}
Number of matches won:{matches_won}
Number of matches lost:{matches-matches_won}
Number of matches won without losing a set and the percentage of it in all matches won:{perfect_match},{perfect_match/matches_won*100:.2f}%
Number of matches finished in 5 sets and the percentage of it in all matches:{long_match},{long_match/matches*100:.2f}%
Highest difference between the total points won and the total points lost:{max_difference}
Team with the highest point difference:{highest_team}""")








