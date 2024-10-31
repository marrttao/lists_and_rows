def number_of_word(row, word):
    count = 0
    word = word.lower()
    for i in range(len(row)):
        for char in row[i].lower():
            if char == word:
                count += 1
    print(f"{word} {count} times in the row")

if __name__ == '__main__':
    _row = []
    while True:
        element = input("Fill up your row (enter to finish): ")
        if element == "":
            break
        _row.append(element)
    _word = input("word you want to count: ")
    number_of_word(_row, _word)