import datetime
import random
from curses.ascii import isalpha


class Vernam:

    def __init__(self) -> None:
        self.key = ''
        self.timestamp_key = dict()
    
    def encrypt(self, msg):
        key = [random.randint(0, 255) for i in range(len(msg))]
        self.key = key
        cipher = ''
        for a, b in zip(msg, key):
            cipher += chr(ord(a)^b)
        
        now = datetime.datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
        self.timestamp_key.update({timestamp: key})

        return cipher+timestamp

    def decrypt(self, cipher):
        msg = ''
        key = self.timestamp_key[cipher[-19:]]
        for a, b in zip(cipher, key):
            msg += chr(ord(a)^b)
        return msg

vern = Vernam()
c1 = vern.encrypt('meow')
c2 = vern.encrypt('bark')
print(vern.decrypt(c1))