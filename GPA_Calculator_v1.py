#ctto-----RockEt🚀 

# program to calculate the GPA of a student oh! 



number_of_courses=input("How many courses do you offer: ")

total_credits_hours_attempted=0

total_grade_points=0

i=0


while i<int(number_of_courses):
    creditHours=int(input("\nEnter creditHours: "))
    total_credits_hours_attempted+=creditHours
    grade=input("Enter your letter grade: ")
    
    grade=grade.upper()#convert the grat
    if grade== 'A' or grade== 'B' or grade== 'C' or grade== 'C' or grade== 'D' or grade== 'F':
        i+=1#next iteration

        if grade== 'A':
            total_grade_points+=4*creditHours
            grade_points=4*creditHours
            #print ("\n\grade_points:"+str(grade_points))

        elif grade== 'B':
            total_grade_points+=3*creditHours
            grade_points=3*creditHours
            #print ("\n\grade_points:"+str(grade_points))

        elif grade== 'C':
            total_grade_points+=2*creditHours
            grade_points=2*creditHours
            #print ("\n\grade_points:"+str(grade_points))

        elif grade== 'D':
            total_grade_points+=1*creditHours
            grade_points=1*creditHours
            #print ("\n\grade_points:"+str(grade_points))

        elif grade== 'F':
            total_grade_points+=0*creditHours
            grade_points=0*creditHours
            #print ("\n\grade_points:"+str(grade_points))

        #print ("total_grade_points:"+str(total_grade_points))
        print ("   ----grade_points: "+str(grade_points))

    else:
        print ("Error, the grade should be A,B,C,D or F")


Gpa=total_grade_points/total_credits_hours_attempted

print ("\n\n\ntotal_grade_points: "+str(total_grade_points))

print ("\ntotal_credits_hours_attempted: "+str(total_credits_hours_attempted))

print ("\n\n\nGPA : "+str(Gpa))

