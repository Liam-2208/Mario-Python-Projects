def format(isbn):
    formatted_isbn = ""
    for char in isbn:
        if char.isalnum():
            formatted_isbn += char
    return formatted_isbn

def validate_ISBN(isbn):
    sum = 0
    for i in range(0, len(isbn)-1):
        temp = isbn[i]
        if i % 2 == 0:
            sum += int(temp)*1
        else:
            sum += int(temp)*3
    
    r = sum%10
    if r == 0:
        check_digit = r
        return check_digit == int(isbn[-1])
    else:
        check_digit = 10-r
        return check_digit == int(isbn[-1])

def main():
    formatted_isbn = format("978-7-7915-1754-2")
    valid = validate_ISBN(formatted_isbn)
    print(valid)

if __name__ == "__main__":
    main()