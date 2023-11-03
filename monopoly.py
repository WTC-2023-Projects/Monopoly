import radice as rd

def monopoly():
    pass 

def run_game():
    pass

def menu():
    options = {1: "Add Player", 2: "Start Game"}
    
    for option in options:
        print("{} - {}".format(option, options[option]))
    
    player_input(options)
    
    print(options[option])
def player_input(options):
    option = input("What would you like to do? ")
    
    if int(option) in options:
        return option
    else:
        print("Invalid Option")
        return player_input(options)

if __name__ == "__main__":
    menu()