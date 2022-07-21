from next_games import next_games
print("Welcome to the official Portland Trail Blazers App! 🌹")


def choice():
    option = input("How can we help you today?\n 1 - Next Games\n 2 - Season Tickets\n 3 - Store\n 4 - Social Media\n")

    if option == "1":
        print("Coming soon:\n")
        for game in next_games:
            print(str(next_games[game] + "\n"))
    elif option == "2":
        print ("Season Tickets are still not available, you can get more info at: https://www.nba.com/blazers/seasontickets/")
    elif option == "3":
        print("Coming soon. You can check https://www.nba.com/blazers/ripcityclothing/ for online shopping!")
    elif option == "4":
        print("You can find us in:\n Instagram: @trailblazers\n Twitter: @trailblazers\n TikTok: @trailblazers")
    else:
        print("Option not available.")
        
def another_option():
    option2 = input("Do you want to keep going? ('Y' for Yes, 'N' for No)")
    if option2.upper() == "Y":
        choice()
    elif option2.upper() == "N":
        print("It was a pleasure to help you! #RipCity 🌹")
    else:
        print("Option not available")
        another_option()
        
choice()
another_option()
