from next_games import next_games
print("Welcome to the official Portland Trail Blazers App!")

def choice():
    option = input("How can we help you today?\n 1 - Next Games\n 2 - Season Tickets\n 3 - Store\n")

    if option == "1":
        print("Coming soon:\n")
        for game in next_games:
            print(str(next_games[game] + "\n"))
    elif option == "2":
        print ("Season Tickets are still not available, you can get more info at: https://www.nba.com/blazers/seasontickets/")
    elif option == "3":
        print("Coming soon. You can check https://www.nba.com/blazers/ripcityclothing/ for online shopping!")
    else:
        print("Option not available.")
    
choice()
