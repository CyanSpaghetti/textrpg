import sys, os
from writer import writer
import text as txt
from parser import parser
from player import player
class game:
    def __init__(self):
        self.running = True
        self.writer = writer()
        self.parser = parser(self)
        self.player = player() # change to input normally
    def start(self):
        self.writer.type(text=txt.Intro, color='b', speed=0.02)
    def update(self):
        pass
    def clear(self):
        if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
            os.system("clear")
        elif sys.platform == "win32":
            os.system("cls")
    def input(self):
        playerinput = str(input(self.player.name + '>>> '))
        self.parser.read(playerinput) 
    def write(self):
        pass
    def close(self):
        sys.exit()
    def mainloop(self):
        self.clear()
        self.start()
        print("test")
        while self.running:
            self.update()
            self.input()
            self.write()
            self.clear()
        self.close()