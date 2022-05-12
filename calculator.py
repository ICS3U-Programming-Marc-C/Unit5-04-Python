#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program calculate math operation based on user's choice


# Defining the function that checks the level and return the middle percentage
def calculator(sign, first_dec, second_dec):

    if sign == "+":
        return first_dec + second_dec
    elif sign == "-":
        return first_dec - second_dec
    elif sign == "*":
        return first_dec * second_dec
    elif sign == "/":
        return first_dec / second_dec
    elif sign == "%":
        return first_dec % second_dec


if __name__ == "__main__":
    # Getting the user input
    sign_input = input("Enter the sign of the operation (ex: +, -, *, /, %): ")
    first_input = input("Enter the first number: ")
    second_input = input("Enter the second number: ")

    try:
        # Convert the number to a float
        first_num = float(first_input)
        second_num = float(second_input)

        # Checking the sign and calling the function
        if (
            sign_input == "+"
            or sign_input == "-"
            or sign_input == "*"
            or sign_input == "/"
            or sign_input == "%"
        ):
            result = calculator(sign_input, first_num, second_num)
            print(
                "The result of {} {} {} is {:.2f}".format(
                    first_num, sign_input, second_num, result
                )
            )
        else:
            # In case of a invalid sign inputted
            print("Invalid input. Please enter a sign such as (+, -, *, /, %).")
    except:
        # In case of a invalid number inputted
        print("Invalid numbers. Please enter proper numbers.")
