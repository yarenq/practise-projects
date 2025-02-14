#fix it

def get_data_and_calculate_fan_counts(team_fan_counts):
    cont="y"
    while cont=="y":
        team_name=input()
        try:
            team_fan_counts[team_name] += 1
        except KeyError:
            team_fan_counts[team_name] = 1

        cont=input("is there an another person?")
def display_fan_counts():
    for team_name, fan_count in team_fan_counts.item():
        print(team_name,team_fan_counts[team_name])
def main():
    team_fan_counts={}
    get_data_and_calculate_fan_counts(team_fan_counts)
    diplay_fan_counts(team_fan_counts)
main()