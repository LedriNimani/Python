def calculate(nr1,nr2,operator):

    if operator== "+":
        return nr1+nr2
    elif operatori=="-":
        return nr1-nr2
    elif operatori=="*":
        return nr1*nr2
    elif operatori=="/":
        return nr1/nr2
    else:
        raise ValueError("Invalid operation")

    try:

    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    operatori=input("Enter an operation:+,-,*,/")
    resultati=calculate(num1,num2,operatori)

    print(f"Invalid input {e}")

    except ZeroDivisionError as e:
    print(f"Cannot divide by 0 {e}")

    except Exception as e:
    print(f"Error: {e} ")

    finally:
    print("End of the program")
