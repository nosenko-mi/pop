def get_avg(x: list[int|float]) -> int | float:
    return sum(x)/len(x)


def main():
    
    numbers = []
    while True:
        user_input = input("Enter a number: ")

        if not user_input.isdigit():
            numbers.sort()
            print(numbers)
            avg = get_avg(numbers)
            print(f"Average value: {avg}")
            print(f"Nubers < average: {[i for i in numbers if i < avg]}")
            print(f"Numbers == average: {[i for i in numbers if i == avg]}")
            print(f"Numbers > average: {[i for i in numbers if i > avg]}")
            
            break

        numbers.append(float(user_input))
        print(f"current numbers {numbers}")   

    return


main()