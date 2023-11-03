#places with prices

def place():
    
    Board = [
            Tile("GO"),
            Property("Mediterranean Avenue", 60, 2),
            Tile("Community Chest"),
            Property("Baltic Avenue",60, 8),
            Tile("Income Tax"),
            Property("Reading Railroad", 200, 50),
            Property("Oriental Avenue", 100, 6),
            Tile("Chance"),
            Property("Vermont Avenue", 100, 6),
            Property("Connecticut Avenue", 120, 8),
            Tile("Jail"),
            Property("St. Charles Place", 140, 10),
            Utility("Electric Company", 150, 1),
            Property("States Avenue", 140, 10),
            Property("Virginia Avenue", 160, 12),
            Property("Pennsylvania Railroad", 200, 50),
            Property("St. James Place", 180, 14),
            Community("Community Chest"),
            Property("Tennessee Avenue", 180, 14),
            Property("New York Avenue", 200, 16),
            Tile("Free Parking"),
            Property("Kentucky Avenue", 220, 18),
            Tile("Chance"),
            Property("Indiana Avenue", 220, 18),
            Property("Illinois Avenue", 240, 20),
            Property("B. & O. Railroad", 200, 50),
            Property("Atlantic Avenue", 260, 22),
            Property("Ventnor Avenue", 260, 22),
            ("Water Works", 150, 0),
            Property("Marvin Gardens", 280, 24),
            Jail("Go To Jail"),
            Property("Pacific Avenue", 300, 26),
            Property("North Caroliina Avenue", 300, 26),
            Tile("Community Chest"),
            Property("Pennsylvania Avenue", 320, 28),
            Property("Short Line", 200, 50),
            Chance("Chance"),
            Property("Park Place", 350, 35),
            Tile("Luxury Tax", -100),
            Property("Boardwalk", 400, 50)]

def Property(name_property, price_of_property):
    
    return name_property, price_of_property
    
def Tile(name):
    
    return name

def Utility(place):
    
    return place

def Chance(name):
    
    return name

def Community(name):
    
    return name

def Jail(call):
    return call

def Owned(players, owned_cards):
    return True