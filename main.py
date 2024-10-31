def reverse(row):
    reversed_row = []
    for i in range(len(row) - 1, -1, -1):
        reversed_row.append(row[i])
    return reversed_row


if __name__ == '__main__':
    row = []
    while True:
        element = input("Fill up your row (enter to finish): ")
        if element.isdigit():
            row.append(int(element))
        elif element == "":
            break
        else:
            print("Please enter a valid number.")
    reversed_row = reverse(row)
    print("Original row:", row)
    print("Reversed row:", reversed_row)