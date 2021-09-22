#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user to input the number for the month

def main():
    # this tells the user what month it is when the user inputs a number

    # input
    month_input = int(input("Enter the number for a month (Ex: 3 for March): "))

    # process & output
    if month_input == 1:
        print("This is the month of January!")
    elif month_input == 2:
        print("This is the month of February!")
    elif month_input == 3:
        print("This is the month of March!")
    elif month_input == 4:
        print("This is the month of April!")
    elif month_input == 5:
        print("This is the month of May!")
    elif month_input == 6:
        print("This is the month of June!")
    elif month_input == 7:
        print("This is the month of July!")
    elif month_input == 8:
        print("This is the month of August!")
    elif month_input == 9:
        print("This is the month of September!")
    elif month_input == 10:
        print("This is the month of October!")
    elif month_input == 11:
        print("This is the month of November!")
    elif month_input == 12:
        print("This is the month of December!")
    else:
        print("No idea!")
    print("\nDone.")


if __name__ == "__main__":
    main()
