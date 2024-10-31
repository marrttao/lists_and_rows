import random

def main(): #не знал как назвать функцию решил назвать по обычному
    n = 10
    numbers = [random.randint(-10, 10) for _ in range(n)]
    numbers.sort()
    negative_elements = 0
    zero_elements = 0
    positive_elements = 0

    for element in numbers:
        if element < 0:
            negative_elements +=1
        elif element == 0:
            zero_elements += 1
        else:
            positive_elements += 1

    print(f"Negative elements: {negative_elements}")
    print(f"Zero elements: {zero_elements}")
    print(f"Positive elements: {positive_elements}")
if __name__ == '__main__':
    main()
