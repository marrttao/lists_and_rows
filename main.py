def number_of_word(row, word, replace):
    count = 0
    word = word.lower()
    for i in range(len(row)):
        element = row[i].lower()
        index = 0
        while index < len(element):
            index = element.find(word, index)
            if index == -1:
                break
            row[i] = row[i][:index] + replace + row[i][index + len(word):]
            index += len(word)
    print(row)

if __name__ == '__main__':
    _row = []
    while True:
        element = input("Fill up your row (enter to finish): ")
        if element == "":
            break
        _row.append(element)
    _word = input("word you want to replace: ")
    _replace = input("replacing word: ")
    number_of_word(_row, _word, _replace)