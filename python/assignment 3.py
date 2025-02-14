age=int(input("Enter your age: "))
fee=int(input("Enter your last annual fee: "))
order=int(input("Enter your last team's rank at the end of the regular season: "))


if order>8:
      match=26      #amount of matches played in the regular season
      cost=fee / match           #we make a division to find the cost to the player's team per play
      print(f"Your cost to your team per game played: ${cost:.2f}")
      if age<22:
          print ("You do not have the right to be released (leave your team).")
      else:

           if age==22:
                release=fee*2
           elif age==23:
                release=fee
           elif age==24:
                release=fee/2
           else:
                release=0
           print(f"You have the right to be released (leave your team), your release fee: ${release:.2f}")

else:
    game_played_regular=int(input("Enter the number of games your team played in the playoff season: "))  #inputs the play-off season info for the top 8 teams
    match=26+ game_played_regular  #total amount of games played in regular season and play-off season
    cost = fee / match
    print(f"Your cost to your team per game played: ${cost:.2f}")
    if age<22:
        print("You do not have the right to be released (leave your team).")
    else:

        if age==22:
            release=fee*2
        elif age==23:
            release=fee
        elif age==24:
            release=fee/2
        else:
            release=0
        print(f"You have the right to be released (leave your team), your release fee: ${release:.2f}")







