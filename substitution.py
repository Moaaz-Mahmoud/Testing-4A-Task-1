from ast import Sub
from curses.ascii import islower, isupper
import random; random.seed(21)


alphabet = ''.join(chr(c) for c in range(ord('a'), ord('z')+1))
alphabet_shuffled = ''.join(random.sample(alphabet,len(alphabet)))

mapper = dict(zip(alphabet, alphabet_shuffled))
reverse_mapper = dict(zip(alphabet_shuffled, alphabet))


class Substitution:

    def encrypt(msg):
        cipher = ''
        for c in msg:
            try:
                if islower(c): cipher += mapper[c]
                else: cipher += str.upper(mapper[str.lower(c)])
            except:
                cipher += c
        return cipher

    def decrypt(cipher):
        msg = ''
        for c in cipher:
            try:
                if islower(c): msg += reverse_mapper[c]
                else: msg += str.upper(reverse_mapper[str.lower(c)])
            except:
                msg += c
        return msg