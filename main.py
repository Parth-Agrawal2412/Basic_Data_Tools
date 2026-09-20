

def average_finder():
    choice = int(input("Enter how many numbers you add to find average: "))
    numbers = []
    for i in range(choice):
        num = int(input("Enter your number: "))
        numbers.append(num)
    average = (sum(numbers))/choice
    print(f"The Average of two numbers is {average}")

def students_report_card_generator():
    choice = int(input("Enter how many sujects you want to enter: "))
    subjects = []
    subjects_marks = []
    for i in range(choice):
        subject = input("Enter subject name: ")
        subject_mark = int(input("Enter marks in this subject: "))
        subjects.append(subject)
        subjects_marks.append(subject_mark)
    # print(len(subjects))
    len_of_subject = len(subjects)
    a = 1
    print("S.no     Subject     Marks")
    for i in range(len_of_subject):
        print(f"{a}.        {subjects[i]}           {subjects_marks[i]}")
        a += 1
    percentage = (sum(subjects_marks))/choice
    print(f"The total percentage is {percentage}")



def mean_calculator():
    choice = int(input("Enter how many numbers you add to find mean: "))
    numbers = []
    for i in range(choice):
        num = int(input("Enter your number: "))
        numbers.append(num)
    mean = (sum(numbers))/choice
    print(f"The Average of two numbers is {mean}")