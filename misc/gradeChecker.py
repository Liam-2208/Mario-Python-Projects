def main():
    try:    
        score = int(input('Enter your score [1-100]: '))
        if score > 100 or score < 0:
            print('Enter a valid number.\n')
            main()

        if score >= 90:
            grade = 'A*'
            pass
        elif score >= 80:
            grade = 'A'
            pass
        elif score >=70:
            grade = 'B'
            pass
        elif score >=50:
            grade = 'C'
            pass
        elif score >=30:
            grade = 'D'
            pass
        elif score < 30:
            grade = 'E'
            pass

        if score>=50:
            print(f'You passed.\nGrade: {grade}')
        elif score<50:
            print(f'You failed.\nGrade: {grade}')
    
    except (ValueError, TypeError):
        print('Enter a valid number.\n')
        main()

main()
