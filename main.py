def number_of_word(row, word):
    count = 0
    word = word.lower()
    for i in range(len(row)):
        element = row[i].lower()
        index = 0
        while index < len(element):
            index = element.find(word, index) #Знаю как работате если нужно будет смогу обьяснмить
            if index == -1:
                break
            count += 1
            index += len(word)
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