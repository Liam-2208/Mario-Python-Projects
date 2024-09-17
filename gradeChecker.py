def main():
    try:
        score = int(input('Enter your score [0-100]: '))
    except ValueError:
        print('Enter a valid number.')
        main()
        
    if score > 100 or score < 0:
        print('Invalid input.\n')
        main()

    if score >= 90:
        grade = 'A*'
    elif score >= 80:
        grade = 'A'
    elif score >=70:
        grade = 'B'
    elif score >=50:
        grade = 'C'
    elif score >=30:
        grade = 'D'
    else:
        grade = 'E'

    if score>=50:
        print(f'You passed.\nGrade: {grade}')
    else:
        print(f'You failed.\nGrade: {grade}')

main()
