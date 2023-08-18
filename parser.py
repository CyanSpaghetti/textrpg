
class parser:
    def __init__(self, game):
        self.game = game
    def read(self, command):
        match command: 
            case "exit":
                self.game.running = False