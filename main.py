import readchar

def main():
    print(
'''
Welcome to Money Matters!

[Mode Selection]
1. Bonds
2. Net income
3. Installments
4. Splitting

Key in your mode:

'''
    )
    key = int(readchar.readkey())
    match key:
        case 1:
            print("Bonds")
        case 2:
            print("Net income")
        case 3:
            print("Installments")
        case 4:
            print("Splitting")
        case _:
            print("Invalid selection")
 
if __name__ == "__main__":
    main()
