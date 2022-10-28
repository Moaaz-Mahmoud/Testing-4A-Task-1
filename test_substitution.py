import unittest
from substitution import Substitution


messages = [
    'a',
    'b',
    'm',
    'q',
    'r',
    'w',
    'z',
    'A',
    'Q',
    'W',
    'Z',
    'aaa',
    'ZZZ',
    'bark',
    ' The-quick,brown*fox\jumps9over  the lazy dog.'
]
ciphers = [
    'f',
    'n',
    'o',
    'r',
    's',
    'k',
    'm',
    'F',
    'R',
    'K',
    'M',
    'fff',
    'MMM',
    'nfsz',
    ' Hgu-rxtwz,nsakd*jae\qxolb9avus  hgu ifmc yap.'
]


class TestSubstitution(unittest.TestCase):
    
    def test_encrypt(self):
        for i in range(len(ciphers)):
            self.assertEqual(Substitution.encrypt(messages[i]), ciphers[i])
    
    def test_decrypt(self):
        for i in range(len(ciphers)):
            self.assertEqual(Substitution.decrypt(ciphers[i]), messages[i])


if __name__ == '__main__':
    unittest.main()