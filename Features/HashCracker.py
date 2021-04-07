from Features.base import FeatureBase
import hashlib
from string import ascii_lowercase
from string import ascii_uppercase
import itertools
import threading
import time
import os

letters = ascii_uppercase + ascii_lowercase + '1234567890'
tested = 0
threads = []
found = False
FoundPassword = ''
totalPosible = 0


def calc_total():
  total = 0

  return total

def ArrayToString(arr):
  string = ''
  for a in arr:
    string = string+a
  return string

def do_CheckPassword(keywrods, hashPassword):
  global tested
  global found
  global FoundPassword
  for i in keywrods:
    if found == True:
      return True
    string = ArrayToString(i)
    hashedString = hashlib.md5(bytes(string, 'utf-8')).hexdigest()
    tested+=1
    if hashedString == hashPassword:
      found = True
      FoundPassword = string
      print('\nPassword is: '+string)

class Feature(FeatureBase):
    def __init__(self):
        super().__init__(
            name="Hash Cracker",
            description="This will crack a hashed password.",
            options=[
                {
                    "message": "Hashed Password: ",
                    "type": "input",
                    "name": "hash"
                },
                {
                    "message": "Min Letters: ",
                    "type": "input",
                    "name": "min"
                },
                {
                    "message": "Max Letters: ",
                    "type": "input",
                    "name": "max"
                }
            ]
        )

    def function(self, options):
        global letters
        global tested
        global threads
        global found
        global FoundPassword
        global totalPosible
        letters = ascii_uppercase + ascii_lowercase
        tested = 0
        threads = []
        found = False
        FoundPassword = ''
        totalPosible = 0

        print("Starting Threads...")

        for i in range(int(options['min'])+1):
            if i < int(options['min']):
                pass
            else:
                keywords = itertools.product(letters, repeat = i)
                th = threading.Thread(target=do_CheckPassword, args=(keywords, options['hash']), daemon=True)
                th.start()
                threads.append(th)


        print("Started threads. \nWaiting to find password...")
        while found == False:
            print(f"\rTested Passwords: {str(tested)}| Current Threads: {len(threads)}", end='', flush=True)

        input('Press any key to return to main screen.')
