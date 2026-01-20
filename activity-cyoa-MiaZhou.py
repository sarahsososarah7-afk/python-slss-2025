# Choose Your Own Adventure
# Mia zhou
# 24 September

# Choose your own adventure story focusing
# on using variables and branching/conditionals

print("You are in the middle of a rain forest alone.")
print("There's a key on the ground right beside your foot.")
print("There's also a house with a locked door to your left.")
print("And there's a locked wooden box sitting on top of a bush to your right.")
house_box = input("Do you want to use the key to open the house or box?")

if house_box == "Open house":
    print("House.")

    print(
        "As you unlock the house, you take a few steps inside and discover a dark hallway with a huge window."
    )
    print(
        "Step by step, you walk in deeper into the hallway which leads up to tiny baby grizzly bear."
    )
    print(
        "Very slowly, you approach the baby bear and it suprisingly starts greeting you by talking to you."
    )
    talk_window = input("Do you talk back to the bear or climb out the window?")

    if talk_window == "Talk back":
        print("Talk.")

        print(
            "You and the bear slowly gets to know each other and he finds out you're lost in the forest."
        )
        print(
            "The kind bear offers to guide you ut of the forest with the help of his bear friends"
        )
        print(
            "Trusting the bears, you follow them slowly into the forest again where they lead you to a cave."
        )
        print("Suprisingly, you see that you have connection on you phone now.")
        stay_cave = input(
            "Do you go into the cave with the bears or stay outside and use your phone to call for help?"
        )

        if stay_cave == "Stay":
            print("Stay.")

            print(
                "Staying outside the cave allowed you to go one your phone and call for help."
            )
            print(
                "You called 911 to come rescue you, but they said it will take them at least 45 minutes to reach you."
            )
            Maps_wait = input(
                "Do you use Google Maps and try to rescue yourself, or do you wait for 911 to come rescue you?"
            )

            if Maps_wait == "Maps":
                print("Maps.")
                print("Opening the Google Maps app, you start to follow the arrows.")
                print("Walking where the arrow is leading you, you finally see an exit sign to leave the forest.")
                print("After hours, you were finally able to leave the forest.")

            else:
                print("Wait.")
                print("You wait and wait then about 25 mins ;ater, 911 finally comes.")
                print("They ask you a bunch of questions like if you were hurt and such.")
                print("Five mins later, they finally take you out of the forest in the ambulance and you are at home in no time.")

        else:
            print("Cave.")
            print(
                "Hesitantly, you walk into the cave with the bears and you discover a whole cave full of food."
            )
            print("Too tired you lay down on the ground and fell asleep.")
            print(
                "Seeing that the bears didn't harm you while you were asleep, you trust them and stay with the bears forever."
            )
            print(
                "As time goes on, you grow with the bears and you guys become family!"
            )
    else:
        print("Window")
        print("Scared, you run to the wndow and climbs out of it in no time.")
        print(
            "Running as fast as you can, you found yourself beside a river full of beautiful rocks and fish."
        )
        print(
            "Tired, you take out your waterbottle to fill it up with water and you see a compass on the ground."
        )
        print("After drinking water, you check the compass and it works!")
        print(
            "You decide to follow the compass and it slowly takes you out of the forest."
        )
        print(
            "After hours, you finally made it out of the forest and into a small coffee shop near by; drinking a latte and eating a muffin."
        )
else:
    print("Box.")

    print(
        "As you unlock the wooden box, a huge glowig beam of light lights up your face."
    )
    print(
        " Inside the box, you find a really torn map, but all the important details and routes are still visible."
    )
    print(
        "Taking the map, do you follow it and exit route and leave the rain forest or do you follow the route that leads you to a treasure box?"
    )
    exit_treasure = input("Are you going to exit the forest or find the treasure box")

    if exit_treasure == "Exit":
        print("Exit.")
        print("Reading and following the map, you try and walk towards the exit.")
        print("After countless hours, you finally made it out!")

    else:
        print("Treasure")
        print("Excited, you run along the route that leads you to the treasure box.")
        print("Finally, you find the treasure box and you see that there's nothing inside.")
        print("Then you realize you've been pranked by the last person who was lost in this forest.")

