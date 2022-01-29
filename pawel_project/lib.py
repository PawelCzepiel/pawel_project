# pawel_project/lib.py

import datetime
from termcolor import colored

def try_me():
    return print(colored(f'THE TIME IS: {datetime.datetime.now().time()}','red'))