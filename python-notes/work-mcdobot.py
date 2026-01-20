## Work - McDoBot
# Author: Sarah
# 6 October

# It asks if you want fries with your meal.
fries_reply = input("Do you want fries with your meal? ").lower().strip("!,.? ")

# It should accept  Yes/yes  or  No/no
# as inputs, and reply appropriately depending on the answer.
# If the user inputs anything else,
# it should repeat back their answer and
# say that it does not understand.
if fries_reply == "yes":
    print("Here is your meal with fries.")
elif fries_reply == "no":
    print("Here is your meal without fries.")
else:
    print(f'I don\'t understand what "{fries_reply}" means.')
