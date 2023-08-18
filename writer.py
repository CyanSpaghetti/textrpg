import os, time
from colorama import init, Fore, Back, Style
init()

class writer:
    def __init__(self):
        pass
    def type(self, text, color, speed=0.02):
        match(color):           
            case 'r':
                print(Fore.RED)
                for index in range(len(text)-1):
                    print(text[index], end='', flush=True)
                    time.sleep(speed)
            case 'g':
                print(Fore.GREEN)
                for index in range(len(text)-1):
                    print(text[index], end='', flush=True)
                    time.sleep(speed)
            case 'b':
                print(Fore.BLUE)
                for index in range(len(text)-1):
                    print(text[index], end='', flush=True)
                    time.sleep(speed)
            case _:
                print(Fore.RESET)
                for index in range(len(text)-1):
                    print(text[index], end='', flush=True)
                    time.sleep(speed)
        print(Fore.RESET)

            