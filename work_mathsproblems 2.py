# Math stuff with python
# Author: Sarah
# Date: Nov 12 2023

# Description: This file contains various mathematical functions implemented in Python.


# Question 1


def main():
    current_age = int(input("How old are you?"))
    # Difference between this year and 2049
    age_in_2049 = current_age + 31
    # Results
    print(f"You will be {age_in_2049} in 2049")

    # Question 2
    # Get judges to vote
    print("give me a score from 0-10 half scores are allowed")
    score1 = float(input("Judge 1: 10"))
    score2 = float(input("Judge 2: 7"))
    score3 = float(input("Judge 3: 6"))
    score4 = float(input("Judge 4: 8"))
    score5 = float(input("Judge 5: 9"))

    average_score = (score1 + score2 + score3 + score4 + score5) / 5
    #  final score
    print(f"Your Olympic score is: {average_score}")

    # Question3

    """Ask customer if they
    want burger and fries
    then adds 14% of tax"""

    burger_reply = input("Would like a burger for $5 yes/no").lower().strip("!,.? ")
    if burger_reply == "yes":
        burger_price = 5
        print("Okay we will add burger!")
    else:
        burger_price = 0
        print("Okay got it no burger")

    # Ask the customer if they want fries
    fries_reply = input("Would like fries for $3 yes/no").lower().strip("!,.? ")
    if fries_reply == "yes":
        fries_price = 3
        print("Okay we will add fries!")
    else:
        fries_price = 0
        print("Okay got it no fries")

        # Calculate total before tax
        subtotal = burger_price + fries_price
        # Add the 14% tax
        tax = subtotal * 0.14
        # Final cost
        total_price = subtotal + tax
        print(f"Your total including tax will be: {total_price}")


if __name__ == "__main__":
    main()
