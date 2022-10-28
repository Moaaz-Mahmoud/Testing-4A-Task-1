from curses.ascii import isalpha
import re


class Vigenere:

    def __init__(self, key):
        self.key = key

    def encrypt(self, msg):
        cipher = ''
        skip = 0
        for i in range(len(msg)):
            if not isalpha(msg[i]):
                cipher += msg[i]
                skip += 1
                continue
            j = (i-skip)%len(self.key)
            c = chr(
                (ord(msg[i]) + ord(self.key[j]) - ord('a')*2) % 26 
                + ord('a')
            )
            cipher += c
        return cipher

    def decrypt(self, cipher):
        pass

