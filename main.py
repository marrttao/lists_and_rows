def number_of_letters_and_numbers(row):
    numbers_value = 0
    letters_value = 0
    for element in row:
        if element.isalpha():
            letters_value += len(element)
        elif element.isdigit():
            num = int(element)
            if num < 9:
                numbers_value += 1
            else:
                while num > 9:
                    numbers_value += 1
                    num = num // 10
                numbers_value += 1  # for the last digit
    print(f"letters value{letters_value}")
    print(f"numbers_value{numbers_value}")

if __name__ == '__main__':
    _row = []
    while True:
        element = input("Fill up your row (enter to finish): ")
        if element == "":
            break
        _row.append(element)
    number_of_letters_and_numbers(_row)