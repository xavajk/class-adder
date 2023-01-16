import sys
import time

import class_bot

if __name__ == '__main__':
    if sys.argv[1] == '--help':
        print('Username and Password fields should be surrouned by quotes ("")')
        print('Classes.csv should include only the course numbers separated by commas (,)')
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        file = sys.argv[3]

    try:
        class_bot.login(username, password)
        class_bot.pick_quarter()
        class_bot.add_classes(file)

    except:
        print('Usage: python3 main.py ["Username"] ["Password"] [Classes.csv]')
        print('For help with command line arguments use: python3 main.py --help')