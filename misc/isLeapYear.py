def main():
    isLeapYear = False
    try:
        year = int(input('Enter a year: '))
        if year == 0:
            isLeapYear = True

        if (year%4 == 0 and year%100 != 0) or (year%100 == 0 and year%400 == 0):
            isLeapYear = True

        if isLeapYear:
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year.')

    except ValueError:
        print('Enter a valid integer.\n')
        main()

main()
