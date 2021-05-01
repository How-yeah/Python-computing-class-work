while True:
    year = int(input('Input a year: '))

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("It's a leap year")
    else:
        print("It's not a leap year")
