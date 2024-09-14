from collections import Counter

def main():
    
    user_input = input("Enter a message: ")
    
    if len(user_input) < 1:
        print("No message provided")
        return

    res = Counter(user_input)
    repeated_keys = sorted([k for k, v in res.items() if v > 1])

    print(len(repeated_keys))
    if len(repeated_keys) == 0:
        print(None)
    else:
        for k in repeated_keys:
            print(k, end=" ")
        print("")
    
    return


main()