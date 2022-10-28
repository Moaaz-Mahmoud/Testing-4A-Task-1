from curses.ascii import isupper


is_alpha = lambda c : ord(c) in range(ord('a'), ord('z')+1) or ord(c) in range(ord('A'), ord('Z')+1)


class Caesar:

    def encrypt(msg, k):
        k = k%26
        cipher = ''
        for c in msg:
            if not is_alpha(c):
                cipher += c
                continue
            c_to_add = chr(ord(c) + k)
            if not is_alpha(c_to_add) or isupper(c) != isupper(c_to_add): 
                c_to_add = chr(ord(c_to_add) - 26)
            cipher += c_to_add
        return cipher

    def decrypt(cipher, k):
        k = k%26
        msg = ''
        for c in cipher:
            if not is_alpha(c):
                msg += c
                continue
            c_to_add = chr(ord(c) - k)
            if not is_alpha(c_to_add) or isupper(c) != isupper(c_to_add): 
                c_to_add = chr(ord(c_to_add) + 26)
            msg += c_to_add
        return msg

Caesar.decrypt('z', 1)