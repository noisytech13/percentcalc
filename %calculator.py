#This is noisytech13's python program file
#licence under  noisytech13
#owner = noisytech13
import os
import time
import sys
import colorama
from colorama import init,Fore, Back, Style

colorama.init()

def slowsprint(s):
    for c in s+ '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2./20)
slowsprint("Hello, My name is noisytech13 \n")
name = input("What is your name?\n==>")
slowsprint("Hello " + name )
def calculate_total_marks(grades):
    grade_values = {
        'A+': 95,
        'A': 90,
        'A-': 85,
        'B+': 80,
        'B': 75,
        'B-': 70,
        'C+': 65,
        'C': 60,
        'C-': 55,
        'D+': 50,
        'D': 45,
        'D-': 40,
        'F': 0
    }
    
    total_marks = sum(grade_values.get(grade, 0) for grade in grades)
    return total_marks

# Example usage
slowsprint("[ENTER EACH GRADE IN CAPITAL LETTER SEPERATED BY COMAS]")
slowsprint("[example='A+,A+,A+,A,A,B+,B+,B,C+,C']")
grades = str(input("enter your grade="))
total_marks = calculate_total_marks(grades)
print("\n")
print("Total Marks:", total_marks)

percen = total_marks/1000*100
tagu = total_marks
print("\n")
print("YOUR TOTAL MARK IS=" ,tagu,"/1000")
print("\n")
print("The Percentage is=",percen)

#grades = ['A', 'A', 'B+', 'A', 'B', 'A', 'C', 'C+', 'C+', 'C+',]




create = name.capitalize()+'.txt'
if os.path.exists("logs"):
		pass
else:
		os.mkdir("logs")

f = open("logs/"+create,'a')
f.write("Name: "+name.capitalize() + '\n')
#f.write("\nsumu: "+sumu())
f.write("The percentage is=")
f.write(str(percen) + "%")


#f.write(str(tagu))
#file.write(str(number) + '\n')
#file.write(str(number))
#file_path = 'number.txt'
#file = open(file_path, 'w')



