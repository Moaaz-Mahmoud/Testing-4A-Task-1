import unittest
from caesar import Caesar


class TestCaesar(unittest.TestCase):
    
    def test_encrypt_single_char_k_1(self):
        self.assertEqual(Caesar.encrypt('a', 1), 'b')
        self.assertEqual(Caesar.encrypt('b', 1), 'c')
        self.assertEqual(Caesar.encrypt('r', 1), 's')
        self.assertEqual(Caesar.encrypt('x', 1), 'y')
        self.assertEqual(Caesar.encrypt('y', 1), 'z')
        self.assertEqual(Caesar.encrypt('z', 1), 'a')

    def test_encrypt_single_char_k_2(self):
        self.assertEqual(Caesar.encrypt('a', 2), 'c')
        self.assertEqual(Caesar.encrypt('b', 2), 'd')
        self.assertEqual(Caesar.encrypt('h', 2), 'j')
        self.assertEqual(Caesar.encrypt('x', 2), 'z')
        self.assertEqual(Caesar.encrypt('y', 2), 'a')
        self.assertEqual(Caesar.encrypt('z', 2), 'b')
    
    def test_encrypt_single_char_k_any(self):
        self.assertEqual(Caesar.encrypt('a', 7), 'h')
        self.assertEqual(Caesar.encrypt('a', 25), 'z')
        self.assertEqual(Caesar.encrypt('v', 25), 'u')
        self.assertEqual(Caesar.encrypt('s', 26), 's')
        self.assertEqual(Caesar.encrypt('a', 52), 'a')
        self.assertEqual(Caesar.encrypt('d', 54), 'f')
        self.assertEqual(Caesar.encrypt('d', 7), 'k')
    
    def test_encrypt_works_withmulti_char_k_any_all_alpha(self):
        self.assertEqual(Caesar.encrypt('abcdxyz', 1), 'bcdeyza')
        self.assertEqual(Caesar.encrypt('abcdxyz', 4), 'efghbcd')
        self.assertEqual(Caesar.encrypt('meow', 25), 'ldnv')
        self.assertEqual(Caesar.encrypt('moaaz', 3), 'prddc')

    def test_encrypt_non_alpha(self):
        self.assertEqual(Caesar.encrypt(' a b y z ', 2), ' c d a b ')
        self.assertEqual(Caesar.encrypt('#cats meow, haha!$', 27), '#dbut nfpx, ibib!$')
    
    def test_encrypt_upper_case(self):
        self.assertEqual(Caesar.encrypt('ABC abc- XYZ -xyz', 3), 'DEF def- ABC -abc')
        self.assertEqual(Caesar.encrypt('I\'m a meowing cat!', 1), 'J\'n b nfpxjoh dbu!')
        self.assertEqual(Caesar.encrypt('ABYZ', 1), 'BCZA')

    def test_decrypt_single_char_k_1(self):
        self.assertEqual(Caesar.decrypt('a', 1), 'z')
        self.assertEqual(Caesar.decrypt('b', 1), 'a')
        self.assertEqual(Caesar.decrypt('r', 1), 'q')
        self.assertEqual(Caesar.decrypt('x', 1), 'w')
        self.assertEqual(Caesar.decrypt('y', 1), 'x')

    def test_decrypt_rest(self):
        self.assertEqual(Caesar.decrypt('abc xyz', 1), 'zab wxy')
        self.assertEqual(Caesar.decrypt('Meow, meow! I\'m a cow!', 1), 'Ldnv, ldnv! H\'l z bnv!')
        self.assertEqual(Caesar.decrypt('Meow', 5), 'Hzjr')
        self.assertEqual(Caesar.decrypt('  mEOW ', 26), '  mEOW ')
        self.assertEqual(Caesar.decrypt('  mEOW ', 286), '  mEOW ')
        self.assertEqual(Caesar.decrypt('CaT mEoW', 25), 'DbU nFpX') # Important
        self.assertEqual(Caesar.decrypt('!@#', 152), '!@#') # Important


if __name__ == '__main__':
    unittest.main()