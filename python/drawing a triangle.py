def draw_line(character,length):
    for counter in range(length):
        print(character,end="")

def main():
    height=int(input("enter the height of the triangle"))
    for row_number in range(1,height+1):
        draw_line(" ",height-row_number)
        draw_line("*",row_number*2-1)
        draw_line(" ",height-row_number)
        print()


main()
