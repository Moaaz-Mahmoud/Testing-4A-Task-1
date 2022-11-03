import random
from curses.ascii import isalpha


class Vernam:
    
    def encrypt(self, msg):
        key = [random.randint(0, 255) for i in range(len(msg))]
        self.key = key
        cipher = ''
        for a, b in zip(msg, key):
            cipher += chr(ord(a)^b)
        return cipher

    def decrypt(self, cipher):
        msg = ''
        key = self.key
        for a, b in zip(ciph, key):
            msg += chr(ord(a)^b)
        return msg


vern = Vernam()
ciph = vern.encrypt('meow')
print(ciph)
print(vern.decrypt(ciph))