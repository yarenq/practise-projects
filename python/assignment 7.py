def take_points(archer_count, shots, winds, points, all_archers_points, loop): #a function that takes the values of points, determines whether they are valid or not, counts the missed shots and takes the names of winds
    global missed_shots
    missed_shots=0
    for shot in range(shots):
        for archer in range(archer_count):
            while loop==True: #loops thorough the try/except block until the valid data is entered
                try:
                    point = int(input(f"Please enter the point earned for {archer + 1}. archer's {shot + 1}. shot: "))
                    while point not in points:
                        print("Invalid data entry, please try again.")
                        point = int(input(f"Please enter the point earned for {archer + 1}. archer's {shot + 1}. shot: "))
                    else:
                        break
                except ValueError:
                    print("Invalid data entry, please try again.")
                    continue
                break
            all_archers_points[archer][point] += 1
            if point == 0:
                missed_shots += 1
                wind_name = input("Please enter the name of the wind blowing: ")
                while loop==True:
                    if wind_name in winds:
                        winds[wind_name] += 1
                        break
                    else:
                        print("Invalid data entry, please try again.")
                        wind_name = input("Please enter the name of the wind blowing: ")
    return missed_shots
def display_table(winds,points,archer_count,all_archers_points,points_count ): #a function that displays the statistics of the data taken from the first function
    print("Archer Reg No  ", end=" ") #first line of the table
    for point in points:
        print(f"{point:4}P",end=" ")
    print("Total Points")
    print("---------------",end=" ") #second line of the table
    for k in range(points_count):
        print("-----",end=" ")
    print("------------")
    column_total=[0]*points_count
    for reg_no in range(archer_count): #the for loop prints out the number of shots in different number of points for every archer
        print(f"{reg_no+1:<15}",end=" ")
        total_points=0
        for point_no in points:
            print(f"{all_archers_points[reg_no][point_no]:5}",end=" ")
            column_total[point_no]+=all_archers_points[reg_no][point_no]
            total_points+=point_no*all_archers_points[reg_no][point_no]
        print(f"{total_points:11}")
    print("All Archers(%) ",end=" ")
    for i in points: #prints out the percentages
        print(f"{column_total[i]/sum(column_total)*100:5.2f}",end=" ")
    print("")
    print("")
    print("")
    missed_shots_rate={}
    for i in winds:
        missed_shots_rate[i]=winds[i]/missed_shots*100
    print("""Wind Name    Missed Shot Rate(%)
----------- -------------------""")
    for key in missed_shots_rate:
        print(f"{key:11}  {missed_shots_rate[key]:<19.2f}")
def main():
    loop=True
    while loop==True: #loops thorough the try/except block until the valid data is entered
        try:
            MIN_NUMBER_OF_ARCHERS = 10
            archer_count = int(input("Please enter the number of archers: "))
            while archer_count < MIN_NUMBER_OF_ARCHERS:
                print("Invalid data entry, please try again.")
                archer_count = int(input("Please enter the number of archers: "))
            else:
                break
        except ValueError:
            print("Invalid data entry, please try again.")
            continue
        break
    while loop==True:
        try:
            shots = int(input("Please enter the number of shots: "))
            while shots<0:
                print("Invalid data entry, please try again.")
                shots = int(input("Please enter the number of shots: "))
            else:
                break
        except ValueError:
            print("Invalid data entry, please try again.")
            continue
        break

    winds = {"North": 0, "Northeaster": 0, "Easterly": 0, "Southeaster": 0, "South": 0, "Southwester": 0, "Westerly": 0,
             "Northwester": 0} #defines the list of valid wind names
    points = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] #defines the list of valid points
    points_count = len(points)
    all_archers_points = []
    for i in range(archer_count): #creates 2d list of number of archers and points they have earned
        archers_points = [0] * points_count
        all_archers_points.append(archers_points)
    take_points(archer_count, shots, winds, points, all_archers_points, loop)
    display_table(winds, points, archer_count, all_archers_points, points_count)
main()