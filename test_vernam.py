import unittest
from vernam import Vernam


vern = Vernam()


class TestVernam(unittest.TestCase):

    def test_all(self):
        
        msg = 'meow'
        self.assertEqual(vern.decrypt(vern.encrypt(msg)), msg)

        msg = 'Beep, beep! I\'m a sheep!'
        self.assertEqual(vern.decrypt(vern.encrypt(msg)), msg)
        
        msg = 'Meow, meow! I\'m a cow!'
        self.assertEqual(vern.decrypt(vern.encrypt(msg)), msg)
        
        msg = 'SF fma  klf fE: wem femfcDS:F< '
        self.assertEqual(vern.decrypt(vern.encrypt(msg)), msg)


if __name__ == '__main__':
    unittest.main()