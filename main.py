def reverse(row):
    reversed_row = []
    for i in range(len(row) - 1, -1, -1):
        reversed_row.append(row[i])
    print("Row:", row)
    print("Reversed row:", reversed_row)


if __name__ == '__main__':
    _row = []
    while True:
        element = input("Fill up your row (enter to finish): ")
        if element == "":
            break
        _row.append(element)
    reverse(_row)