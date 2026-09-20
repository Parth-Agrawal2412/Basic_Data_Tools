

def average_finder():
    choice = int(input("Enter how many numbers you add to find average: "))
    numbers = []
    for i in range(choice):
        num = int(input("Enter your number: "))
        numbers.append(num)
    average = (sum(numbers))/choice
    print(f"The Average of two numbers is {average}")

average_finder()