student_id=int(input("Enter your student ID"))
name=input("Enter your name and surname")
theoretical_first=float(input("Enter weekly theoretical course hours of the first course"))
practical_first=float(input("Enter weekly practical course hours of the first course"))
ects_first=float(input("Enter ECTS credits of the first course"))
grade_first=float(input("Enter term grade of the first course"))
theoretical_second=float(input("Enter weekly theoretical course hours of the second course"))
practical_second=float(input("Enter weekly practical course hours of the second course"))
ects_second=float(input("Enter ECTS credits of the second course"))
grade_second=float(input("Enter term grade of the second course"))
total_local_credits=theoretical_first+theoretical_second+(practical_second+practical_first)/2
total_ects_credits=ects_second+ects_first
local_wgpa=(theoretical_first+practical_first/2)/total_local_credits*grade_first+(theoretical_second+practical_second/2)/total_local_credits*grade_second
ects_wgpa=ects_first/total_ects_credits*grade_first+ects_second/total_ects_credits*grade_second
print("Student id:",student_id)
print("Name and surname:",name)
print("Total amount of local credits taken this semester:",total_local_credits)
print("Total amount of ECTS credits taken this semester:",total_ects_credits)
print("WGPA based on local credit at the end of this semester:",local_wgpa)
print("WGPA based on ECTS at the end of this semester:",ects_wgpa)
