def calculate_result(marks):

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\n----- STUDENT RESULT -----")
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)


marks = []

for i in range(5):
    mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

calculate_result(marks)
