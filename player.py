import random 

class player:
    def __init__(self):
        self.name = gen_player.name()
        
class gen_player:
    def name() -> str:
        names = ["Bob", "John", "Carl", "Paul"]
        return names[random.randint(0, len(names))]
    