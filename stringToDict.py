def stringToDict(s):
    dict = {}
    for char in s:
        if char not in dict:
            dict[char] = 0
            dict[char] +=1
        elif char in dict:
            dict[char] +=1
    return dict

def main():
    s = input("Enter a string: ")
    charCounts = stringToDict(s)
    print(charCounts)

if __name__ == "__main__":
    main()