#PrintStudentGrades.py
from Student import Student
def main():
    filename = input('Enter the input filename: ')
    student_file = open(filename, 'r')
    students = []
    total_score = 0
    average = 0
    # Write rest of code here!
    for line in student_file:
        items = line.rstrip().split()
        # items[0] is the firstname
        # items[1] is the lastname
        # items[2] is the grade (as a str)
        g = float(items[2])
        s = Student (items[0], items[1], g)
        students.append (s)
        total_score += g
    student_file.close()
    average = total_score/len(students)
    print ("Average is ", average)
    print (f"{'First':>10s}{'Last':>10s}{'Score':>10s}")
    for x in students:
        print (x)
 
if __name__ == "__main__":
    main()