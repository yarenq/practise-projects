def take_name(archers,MIN_NUMBER_OF_ARCHERS,archers_list):
    try:
        while archers >= MIN_NUMBER_OF_ARCHERS:
            for archer in range(archers):
                name = input(f"Please enter the name of the {archer + 1}. archer: ")
                archers_list.append(name)
            break
        else:
            print("Invalid data entry")
            archers = int(input("Please enter the number of archers (at least 8): "))
    except ValueError:
        print("Invalid data entry")
        archers = int(input("Please enter the number of archers (at least 8): "))
def take_points(archers,archers_list,total_points,count_10,count_x):
    try:
        shots=int(input("Please enter the number of shots given: "))
        for shot in range(shots):
            for archer in range(archers):
                point = int(input(f"Please enter the point of the shot for {archers_list[archer]}'s {shot + 1}. shot:  "))
                if point in [0, 10, 9, 8, 7, 6, 5]:
                    total_points[archer] += point
                    if point == 10:
                        count_10[archer] += 1
                        is_x = input("Is the shot in the X zone? (y/n): ")
                        if is_x == "y":
                            count_x[archer] += 1
                else:
                    print("Invalid data entry")
                    point=int(input(f"Please enter the point of the shot for {archers_list[archer]}'s {shot+1}. shot:  "))
    except ValueError:
        print("Invalid data entry")
        point = int(input(f"Please enter the point of the shot for {archers_list[archer]}'s {shot + 1}. shot:  "))
def rank(archers,total_points,count_10,count_x,archers_list):
    print("""

Rank Name-Surname Points 10 Count X Count
---- ------------ ------ -------- -------
""")
    for i in range(len(total_points)):
        max_points=max(total_points)
        index_of_max = total_points.index(max_points)
        for j in total_points:
            index_of_j = total_points.index(j)
            if j==max_points:
                if count_10[index_of_max]==count_10[index_of_j]:
                    if count_x[index_of_max]<=count_x[index_of_j]:
                        max_points=j
                        index_of_max = index_of_j
                        break
        rank_name=archers_list[index_of_max]
        number_of_10=count_10[index_of_max]
        number_of_x=count_x[index_of_max]
        total_points.remove(max_points)
        count_10.pop(index_of_max)
        archers_list.pop(index_of_max)
        count_x.pop(index_of_max)
        print(i+1,rank_name,max_points,number_of_10,number_of_x)
def main():
    MIN_NUMBER_OF_ARCHERS = 8
    archers = int(input("Please enter the number of archers (at least 8): "))
    archers_list = []
    total_points = [0] * archers
    count_10 = [0] * archers
    count_x = [0] * archers
    take_name(archers,MIN_NUMBER_OF_ARCHERS,archers_list)
    take_points(archers,archers_list,total_points,count_10,count_x)
    rank(archers,total_points,count_10,count_x,archers_list)
main()






