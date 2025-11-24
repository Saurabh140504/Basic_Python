# Smart Student Result Analyzer

# Step1:Create a simple section
print("/Enter A Student Details")
Name =input("Enter a Student Name:  ")
Roll_Num =int(input("Enter a Student Roll Number:  "))
Section =input("Enter a Student Class & Year:  ")

# Step2:Take Subject-Wise marks
print("/Enter a Student Subject_Wise Marks Range is(0,100): ")
Math =int(input("Enter a Math Mark: "))
Physics =int(input("Enter a Physics Mark: "))
Chemistry =int(input("Enter a Chemistry Mark: "))
Biology =int(input("Enter a Biology Mark: "))
English =int(input("Enter a English Mark: "))

# Step3:Calculate Summary
Total_Marks = 500
Sum_Marks = Math + Physics + Chemistry + Biology + English
Average =Sum_Marks /5
Percentge =(Sum_Marks / Total_Marks) *100

# Step4: Subject-Wise Pass&Fail
Failed =[]

if Math <35:
    Failed.append("Math")
elif Physics <35:
    Failed.append("Physics")
elif Chemistry <35:
    Failed.append("Chemistry")
elif Biology <35:
    Failed.append("Biology")
elif English <35:
    Failed.append("English")

if len(Failed) == 0:
    Result ="Student are clear all subject"
else:
    Result ="Failed in: " + ",".join(Failed)

# Step5:Highest & Lowest Marks
Maximum_Subject_Num =max(Math,Physics,Chemistry,Biology,English)
Minimum_Subject_Num =min(Math,Physics,Chemistry,Biology,English)

# Step6:Grade Calculation
if Percentge >= 90:
    Grade ="A++ : Excellent Performance"
elif Percentge >= 80:
    Grade ="A  : Very Good Performance"
elif Percentge >= 70:
    Grade ="B   : Good Performance"
elif Percentge >= 60:
    Grade ="C : Average Performance"
elif Percentge >=35:
    Grade ="D : Improvement Need"
else:
    Grade ="F:(Fail): Hard Work Need"

# Step7: Feedback to Student with Subject
Feedback = []
if Math > 90:
    Feedback.append("Excellent Performance in Math ")
if Physics > 80:
    Feedback.append("Superb in Physics")
if Chemistry >90:
    Feedback.append("Showing Your Class on Chemisty")
if Biology >85:
    Feedback.append("Good in Biology")
if English >60:
    Feedback.append("Improve the English")
if len(Feedback) == 0:
    Feedback.append("General Feedback:Improve Study Time")

print("---------------------Display-------------------------------------------")
print("---------------------Details----------------------------------------")
print("Name of Student:- ",Name)
print("Student Roll_Number:- ",Roll_Num)
print("Student Class & Section:- ",Section)
print("----------------------Marks Summary-------------------------------------")
print("Total Marks:-",Total_Marks)
print("Total obtained Marks:-",Sum_Marks)
print("Average Marks:-",Average)
print("Percentage",Percentge)
print("Grade:-",Grade)
print("Result:-",Result)
print("----------------------Highest & Lowest-----------------------------------------")
print("Maximum marks:-",Maximum_Subject_Num)
print("Minimum marks:-",Minimum_Subject_Num)
print("-----------------------Feedback-------------------------------------------------")
print("Feedback on Marksheet:-",Feedback)

print("n/----Feedback----")
for item in Feedback:
    print("-",item)