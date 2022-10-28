import unittest
from vigenere import Vigenere


vig = Vigenere('iteam')


class TestVigenere(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(vig.encrypt('hello there'), 'pxpla bairq')

    def test_decrypt(self):
        pass


if __name__ == '__main__':
    unittest.main()