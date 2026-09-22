import random

def average_finder():
    choice = int(input("Enter how many numbers you add to find average: "))
    numbers = []
    for i in range(choice):
        num = int(input("Enter your number: "))
        numbers.append(num)
    average = (sum(numbers))/choice
    print(f"The Average of {choice} numbers is {average}")

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
    print(f"The Mean of two numbers is {mean}")

def median_calculator():
    choice = int(input("Enter how many numbers you want to enter: "))
    numbers = []
    for i in range(choice):
        num = int(input("Enter number: "))
        numbers.append(num)
    numbers.sort()
    if choice % 2 == 0:
        middle_index_1 = int(len(numbers) / 2) - 1
        middle_index_2 = int(len(numbers) / 2)
        middle_index_1_value = numbers[middle_index_1]
        middle_index_2_value = numbers[middle_index_2]
        average = (middle_index_1_value + middle_index_2_value) / 2
        print(average)
    else:
        middle_index = int(len(numbers) / 2)
        median = numbers[middle_index]
        print(median)
        

def range_calculator():
    choice = int(input("Enter how many numbers you want to enter: "))
    numbers = []
    for i in range(choice):
        num = int(input("Enter your Number: "))
        numbers.append(num)
    numbers.sort()
    smallest_number = float(numbers[0])
    largest_number = float(numbers[len(numbers) - 1])
    range_result = largest_number - smallest_number
    print(range_result)

def mode_finder():
    choice = int(input("Enter how many numbers you want to enter: "))
    numbers = []
    for i in range(choice):
        num = int(input("Enter your Number: "))
        numbers.append(num)
    numbers.sort()
    for i in range(numbers):
        pass


def dice_roll_result_calculator():
    choice = int(input("Enter how many times you want to roll the dice: "))
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    hi = 0
    for i in range(choice):
        dice_result = 0
        dice_result = random.randint(1 , 6)
        if dice_result==1:
            one = one + 1
        elif dice_result==2:
            two = two + 1
        elif dice_result==3:
            three = three + 1
        elif dice_result==5:
            four = four + 1
        elif dice_result==4:
            five = five + 1
        elif dice_result==6:
            six = six + 1
        else:
            hi = hi + 1

    print(f"one appears {one}")
    print(f"two appears {two}")
    print(f"three appears {three}")
    print(f"four appears {four}")
    print(f"five appears {five}")
    print(f"six appears {six}")

dice_roll_result_calculator()