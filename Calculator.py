def addition(number1, number2):
    return number1+number2

def subraction(number1, number2):
    return number1-number2

def multiplication(number1, number2):
    return number1*number2

def division(number1, number2):
    try:
        result = number1/number2
        return result
    except ZeroDivisionError as e:
        print("Error:", e)

def calculator():
    while(1):
        print("------------------------------")
        print("----------Calculator----------")
        print("1.Addition")
        print("2.Subraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit\n")
        choice = int(input("Enter the options listed above : "))
        print("\n")
        match choice:
            case 1:
                firstNumber = int(input("First Number :"))
                secondNumber = int(input("Second Number :"))
                result = addition(firstNumber, secondNumber)
                print("------------------------------")
                print(f'Result : {result}')
                print("------------------------------")
                print("\n")

            case 2:
                firstNumber = int(input("First Number :"))
                secondNumber = int(input("Second Number :"))
                result = subraction(firstNumber, secondNumber)
                print("------------------------------")
                print(f'Result : {result}')
                print("------------------------------")
                print("\n")

            case 3:
                firstNumber = int(input("First Number :"))
                secondNumber = int(input("Second Number :"))
                result = multiplication(firstNumber, secondNumber)
                print("------------------------------")
                print(f'Result : {result}')
                print("------------------------------")
                print("\n")

            case 4:
                firstNumber = int(input("First Number :"))
                secondNumber = int(input("Second Number :"))
                result = division(firstNumber, secondNumber)
                print("------------------------------")
                print(f'Result : {round(result, 4)}')
                print("------------------------------")
                print("\n")

            case 5:
                break

            case _:
                print("Invalid Choice...\n")

def main():
    calculator()

if __name__ == '__main__':
    main()