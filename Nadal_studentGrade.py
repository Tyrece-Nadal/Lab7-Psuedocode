#student info
name = input("Enter Your Name:")
section = input("Enter Your Section:")

#student grade
prelim_period = float(input("Enter Your Prelim Grade:"))
if prelim_period <40 or prelim_period >100:
    print("Invalid Output!")
    exit()
midterm_period = float(input("Enter Your Midterms Grade:"))
if midterm_period <40 or midterm_period >100:
    print("Invalid Output!")
    exit()
finals_period= float(input("Enter Your Finals Grade:"))
if finals_period <40 or finals_period >100:
    print("Invalid Output!")
    exit()

#grade calculation
final_grade = float(prelim_period * 0.3333) + (midterm_period * 0.3333) + (finals_period * 0.3333)
final_grade = round (final_grade)
GPA = final_grade 

#GPA calculation and display
if final_grade >=40 and final_grade <=100:
    print(f"Your Final Grade is: {final_grade}")

if GPA >=99 and GPA <=100:
    print("Excellent! Your GPA is: 1.00")
elif GPA >=96 and GPA <=98:
    print("Outstanding! Your GPA is: 1.25")
elif GPA >=93 and GPA <=95:
    print("Superior! Your GPA is: 1.50")
elif GPA >=90 and GPA <=92:
    print("Very Good! Your GPA is: 1.75")
elif GPA >=87 and GPA <=89:
    print("Good! Your GPA is: 2.00")
elif GPA >=84 and GPA <=86:
    print("Satisfactory! Your GPA is: 2.25")
elif GPA >=81 and GPA <=83:
    print("Fairly Satisfactory! Your GPA is: 2.50")
elif GPA >=78 and GPA <=80:
    print("Fair! Your GPA is: 2.75")
elif GPA >=75 and GPA <=77:
    print("Passed! Your GPA is: 3.00")
elif GPA >75:
    print("Failed! Your GPA is 5.0")
else:
    print("Invalid grade. The grade input must be between 40-100")






