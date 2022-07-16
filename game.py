import next_games

print("Welcome to the official Portland Trail Blazers App!")

option = input("How can we help you today?\n 1 - Next Games\n 2 - Season Tickets\n 3 - Store\n")

    
if option == "1":
    print(next_games.next_games)
elif option == "2":
    print ("Not available.")
elif option == "3":
    print("Coming soon. You can check https://www.nba.com/blazers/ripcityclothing/ for online shopping!")
else:
    print("Option not available.")
    
