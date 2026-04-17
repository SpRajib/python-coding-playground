try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num2 / num1
    print("Result is:", result)

except TypeError as e:
    print("Please provide valid input (digit only)",e)

except ZeroDivisionError as err:
    print("Denominator cannot be zero", err)

except ValueError as err:
    print("Invalid input, please enter numeric values only", err)

except Exception as e:
    print("An unexpected error occurred:", e)

else: # if no exception occurs
    print("Division performed successfully.")

finally:
    print("Execution completed.")