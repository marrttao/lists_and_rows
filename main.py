
def number_of_word(row, symbol):
    count = 0
    symbol = symbol.lower()
    for i in range(len(row)):
        for char in row[i].lower():
            if char == symbol:
                count += 1
    print(f"{symbol} {count} times in the row")

if __name__ == '__main__':
    _row = []
    while True:
        element = input("Fill up your row (enter to finish): ")
        if element == "":
            break
        _row.append(element)
    _symbol = input("symbol you want to count: ")[0]
    number_of_word(_row, _symbol)