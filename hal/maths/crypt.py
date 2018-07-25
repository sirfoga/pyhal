# !/usr/bin/python3
# coding: utf-8


""" Perform fast hash, encryption and calculations related to cryptography. """

import binascii
import crypt
import hashlib
from struct import pack

from Crypto import Random
from Crypto.Cipher import ARC2, ARC4, Blowfish, CAST
from Crypto.Hash import SHA224, SHA256
from Crypto.PublicKey import DSA
from Crypto.Random import random


class MD5(object):
    """ md5 hash """

    def __init__(self, string):
        object.__init__(self)
        self.plain = string
        self.hashed = None

    def hash(self):
        """
        :return: hash plaintext
        """

        self.hashed = hashlib.md5(self.plain.encode("utf-8"))
        return self.hashed


class MD6(object):
    """ md6 hash """

    ALLOWED_SIZE = [64, 128, 224, 256, 384, 512]

    def __init__(self, string, size):
        object.__init__(self)
        self.plain = string
        self.size = int(size)
        if self.size not in self.ALLOWED_SIZE:
            raise ValueError(
                "Cannot create MD6 hash of size " + str(self.size))
        self.hashed = None

    def hash(self):
        """
        :return: return md6 hash
        """

        self.hashed = self.hex(self.plain, self.size)
        return self.hashed

    @staticmethod
    def _to_word(i_byte):
        """
        :param i_byte: i-th byte
        :return: to word representation
        """

        length = len(i_byte)
        o_word = []

        for i in range(0, length, 8):
            o_word.append(
                ((i_byte[i + 0] & 0xff) << 56) |
                ((i_byte[i + 1] & 0xff) << 48) |
                ((i_byte[i + 2] & 0xff) << 40) |
                ((i_byte[i + 3] & 0xff) << 32) |
                ((i_byte[i + 4] & 0xff) << 24) |
                ((i_byte[i + 5] & 0xff) << 16) |
                ((i_byte[i + 6] & 0xff) << 8) |
                ((i_byte[i + 7] & 0xff) << 0)
            )

        return o_word

    @staticmethod
    def _from_word(i_word):
        """
        :param i_word: i-th word
        :return: partial hash
        """

        length = len(i_word)
        o_byte = []

        for i in range(length):
            o_byte.append((i_word[i] >> 56) & 0xff)
            o_byte.append((i_word[i] >> 48) & 0xff)
            o_byte.append((i_word[i] >> 40) & 0xff)
            o_byte.append((i_word[i] >> 32) & 0xff)
            o_byte.append((i_word[i] >> 24) & 0xff)
            o_byte.append((i_word[i] >> 16) & 0xff)
            o_byte.append((i_word[i] >> 8) & 0xff)
            o_byte.append((i_word[i] >> 0) & 0xff)

        return o_byte

    @staticmethod
    def _crop(size, data, right):
        """
        :param size: bytes
        :param data: plaintext
        :param right: right index
        :return: crop plaintext to right index
        """

        length = int((size + 7) / 8)
        remain = size % 8

        if right:
            data = data[len(data) - length:]
        else:
            data = data[:length]

        if remain > 0:
            data[length - 1] &= (0xff << (8 - remain)) & 0xff

        return data

    def _hash(self, size, data, key, levels):
        """
        :param size: size of hash
        :param data: plaintext
        :param key: hash key
        :param levels: hash levels
        :return: md6 hash
        """

        b = 512
        c = 128
        d = size
        M = data

        K = key[:64]
        k = len(K)

        while len(K) < 64:
            K.append(0x00)

        K = self._to_word(K)

        r = max(80 if k else 0, 40 + int(d / 4))

        L = levels
        ell = 0

        S0 = 0x0123456789abcdef
        Sm = 0x7311c2812425cfa0
        Q = [
            0x7311c2812425cfa0, 0x6432286434aac8e7, 0xb60450e9ef68b7c1,
            0xe8fb23908d9f06f1, 0xdd2e76cba691e5bf, 0x0cd0d63b2c30bc41,
            0x1f8ccf6823058f8a, 0x54e5ed5b88e3775d, 0x4ad12aae0a6d6031,
            0x3e7f16bb88222e0d, 0x8af8671d3fb50c2c, 0x995ad1178bd25c31,
            0xc878c1dd04c4b633, 0x3b72066c7a1552ac, 0x0d6f3522631effcb
        ]
        t = [17, 18, 21, 31, 67, 89]
        rs = [10, 5, 13, 10, 11, 12, 2, 7, 14, 15, 7, 13, 11, 7, 6, 12]
        ls = [11, 24, 9, 16, 15, 9, 27, 15, 6, 2, 29, 8, 15, 5, 31, 9]

        def f(N):
            S = S0
            A = list(N)

            j = 0
            i = N

            while j < r:
                for s in range(16):
                    x = S
                    x ^= A[i + s - t[5]]
                    x ^= A[i + s - t[0]]
                    x ^= A[i + s - t[1]] & A[i + s - t[2]]
                    x ^= A[i + s - t[3]] & A[i + s - t[4]]
                    x ^= x >> rs[s]

                    if len(A) <= i + s:
                        while len(A) <= i + s:
                            A.append(0x00)

                    A[i + s] = x ^ ((x << ls[s]) & 0xffffffffffffffff)

                S = (((S << 1) & 0xffffffffffffffff) ^ (S >> 63)) ^ (S & Sm)

                j += 1
                i += 16

            return A[(len(A) - 16):]

        def mid(B, C, i, p, z):
            U = ((ell & 0xff) << 56) | i & 0xffffffffffffff
            V = ((r & 0xfff) << 48) | ((L & 0xff) << 40) | \
                ((z & 0xf) << 36) | ((p & 0xffff) << 20) | \
                ((k & 0xff) << 12) | (d & 0xfff)

            return f(Q + K + [U, V] + C + B)

        def par(m):
            P = 0
            B = []
            C = []
            z = 0 if len(m) > b else 1

            while len(m) < 1 or (len(m) % b) > 0:
                m.append(0x00)
                P += 8

            m = self._to_word(m)

            while m:
                B.append(m[:int(b / 8)])
                m = m[int(b / 8):]

            i = 0
            l = len(B)

            while i < l:
                p = P if i == (len(B) - 1) else 0
                C += mid(B[i], [], i, p, z)

                i += 1

            return self._from_word(C)

        def seq(m):
            P = 0
            B = []
            C = [0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
                 0x0, 0x0, 0x0, 0x0]

            while len(m) < 1 or (len(m) % (b - c)) > 0:
                m.append(0x00)
                P += 8

            m = self._to_word(m)

            while m:
                B.append(m[:int((b - c) / 8)])
                m = m[int((b - c) / 8):]

            i = 0
            l = len(B)

            while i < l:
                p = P if i == (len(B) - 1) else 0
                z = 1 if i == (len(B) - 1) else 0
                C = mid(B[i], C, i, p, z)

                i += 1

            return self._from_word(C)

        while True:
            ell += 1
            M = seq(M) if ell > L else par(M)

            if len(M) == c:
                break

        return self._crop(d, M, True)

    @staticmethod
    def _bytes(i_str):
        """
        :param i_str: word
        :return: bytes of word
        """

        i_str = binascii.hexlify(i_str.encode("ascii"))
        o_byte = [int(i_str[i:i + 2], 16) for i in range(0, len(i_str), 2)]

        return o_byte

    def _pre_hash(self, data, size, key, levels):
        """
        :param data: plaintext
        :param size: bytes
        :param key: hash key
        :param levels: hash level
        :return: pre-hash md6
        """

        data = self._bytes(data)
        key = self._bytes(key)

        if size <= 0:
            size = 1
        elif size > 512:
            size = 512

        return self._hash(size, data, key, levels)

    def hex(self, data, size):
        """
        :param data: plaintext
        :param size: bytes
        :return: hex representation
        """

        byte = self._pre_hash(data, size, "", 64)
        hex_str = ""

        for i in byte:
            hex_str += "%02x" % i

        return hex_str

    def raw(self, data, size):
        """
        :param data: plaintext
        :param size: bytes
        :return: raw representation
        """

        byte = self._pre_hash(data, size, key="", levels=64)
        raw_str = ""

        for i in byte:
            raw_str += chr(i)

        return raw_str


class SHA(object):
    """ general SHA hash """

    ALLOWED_SIZE = [1, 224, 256, 384, 512]

    def __init__(self, string, size=ALLOWED_SIZE[0], salt=None):
        object.__init__(self)
        self.plain = string
        self.size = int(size)
        self.salt = salt
        if self.size not in self.ALLOWED_SIZE:
            raise ValueError(
                "Cannot create SHA hash of size " + str(self.size))
        self.hashed = None

    def hash(self):
        """
        :return: hash of given size
        """

        if self.salt is None:
            if self.size == 1:
                self.hash_sha1()
            elif self.size == 224:
                self.hash_sha224()
            elif self.size == 256:
                self.hash_sha256()
            elif self.size == 384:
                self.hash_sha384()
            else:  # 512
                self.hash_sha512()
        else:
            self.hash_sha_salted()

    def hash_sha1(self):
        """
        :return: sha1 hash
        """

        h = SHA(self.plain)
        h.hash()
        self.hashed = h.hashed.hexdigest()
        return self.hashed

    def hash_sha224(self):
        """
        :return: sha224 hash
        """

        h = SHA224.new()
        h.update(self.plain)
        self.hashed = h.hexdigest()
        return self.hashed

    def hash_sha256(self):
        """
        :return: sha256 hash
        """

        h = SHA256.new()
        h.update(self.plain)
        self.hashed = h.hexdigest()
        return self.hashed

    def hash_sha384(self):
        """
        :return: sha384 hash
        """

        h = SHA224.new()
        h.update(self.plain)
        self.hashed = h.hexdigest()
        return self.hashed

    def hash_sha512(self):
        """
        :return: sha512 hash
        """

        h = SHA256.new()
        h.update(self.plain)
        self.hashed = h.hexdigest()
        return self.hashed

    def hash_sha_salted(self):
        """
        :return: sha512 hash
        """

        self.hashed = crypt.crypt(self.plain, self.salt)  # sha512 hash
        return self.hashed


class ARC(object):
    """ ARC hash """

    ALLOWED_SIZE = [2, 4]

    def __init__(self, string, key, size):
        object.__init__(self)
        self.plain = string
        self.key = key
        self.size = int(size)
        if self.size not in self.ALLOWED_SIZE:
            raise ValueError(
                "Cannot create ARC hash of size " + str(self.size))
        self.hashed = None

    def hash(self):
        """
        :return: hash of given size
        """

        if self.size == 2:
            self.hash_ar2()
        else:  # 4
            self.hash_arc4()

    def hash_ar2(self):
        """
        :return: des hash
        """

        iv = Random.new().read(ARC2.block_size)
        cipher = ARC2.new(self.key, ARC2.MODE_CFB, iv)
        self.hashed = iv + cipher.encrypt(self.plain)
        return self.hashed

    def hash_arc4(self):
        """
        :return: des3 hash
        """

        nonce = Random.new().read(16)
        sha_sum = SHA(self.key + nonce)
        sha_sum.hash()
        cipher = ARC4.new(sha_sum.hashed)
        self.hashed = nonce + cipher.encrypt(self.plain)
        return self.hashed


class HMAC(object):
    """ hmac hash """

    def __init__(self, string, key):
        object.__init__(self)
        self.plain = string
        self.key = key
        self.hashed = None

    def hash(self):
        """
        :return: hash plaintext
        """

        h = HMAC(self.key, self.plain)
        h.hash()
        self.hashed = h.hashed.hexdigest()
        return self.hashed


class BLOWFISH(object):
    """ blowfish hash """

    def __init__(self, string, key):
        object.__init__(self)
        self.plain = string
        self.key = key
        self.hashed = None

    def hash(self):
        """
        :return: hash plaintext
        """

        bs = Blowfish.block_size
        iv = Random.new().read(bs)
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv)
        p_len = bs - divmod(len(self.plain), bs)[1]
        padding = [p_len] * p_len
        padding = pack("b" * p_len, *padding)
        self.hashed = iv + cipher.encrypt(self.plain + padding)
        return self.hashed


class IDEA(object):
    """ IDEA hash """

    def __init__(self, string, key):
        self._keys = None
        self.plain = string
        self.hashed = None
        self.change_key(key)

    def hash(self):
        """
        :return: IDEA hash
        """

        self.hashed = hex(self.encrypt())
        return self.hashed

    @staticmethod
    def _mul(x, y):
        """
        :param x: first operand
        :param y: second operand
        :return: x*y
        """

        assert 0 <= x <= 0xFFFF
        assert 0 <= y <= 0xFFFF

        if x == 0:
            x = 0x10000
        if y == 0:
            y = 0x10000

        r = (x * y) % 0x10001

        if r == 0x10000:
            r = 0

        assert 0 <= r <= 0xFFFF
        return r

    def _ka_layer(self, x1, x2, x3, x4, round_keys):
        """
        :param x1: x1
        :param x2: x2
        :param x3: x3
        :param x4: x4
        :param round_keys: rounds
        :return: ka layer
        """

        assert 0 <= x1 <= 0xFFFF
        assert 0 <= x2 <= 0xFFFF
        assert 0 <= x3 <= 0xFFFF
        assert 0 <= x4 <= 0xFFFF
        z1, z2, z3, z4 = round_keys[0:4]
        assert 0 <= z1 <= 0xFFFF
        assert 0 <= z2 <= 0xFFFF
        assert 0 <= z3 <= 0xFFFF
        assert 0 <= z4 <= 0xFFFF

        y1 = self._mul(x1, z1)
        y2 = (x2 + z2) % 0x10000
        y3 = (x3 + z3) % 0x10000
        y4 = self._mul(x4, z4)

        return y1, y2, y3, y4

    def _ma_layer(self, y1, y2, y3, y4, round_keys):
        """
        :param y1: y1
        :param y2: y2
        :param y3: y3
        :param y4: y4
        :param round_keys: rounds
        :return: ma layer
        """

        assert 0 <= y1 <= 0xFFFF
        assert 0 <= y2 <= 0xFFFF
        assert 0 <= y3 <= 0xFFFF
        assert 0 <= y4 <= 0xFFFF
        z5, z6 = round_keys[4:6]
        assert 0 <= z5 <= 0xFFFF
        assert 0 <= z6 <= 0xFFFF

        p = y1 ^ y3
        q = y2 ^ y4

        s = self._mul(p, z5)
        t = self._mul((q + s) % 0x10000, z6)
        u = (s + t) % 0x10000

        x1 = y1 ^ t
        x2 = y2 ^ u
        x3 = y3 ^ t
        x4 = y4 ^ u

        return x1, x2, x3, x4

    def change_key(self, key):
        """
        :param key: new key
        :return: change key
        """

        assert 0 <= key < (1 << 128)
        modulus = 1 << 128

        sub_keys = []
        for i in range(9 * 6):
            sub_keys.append((key >> (112 - 16 * (i % 8))) % 0x10000)
            if i % 8 == 7:
                key = ((key << 25) | (key >> 103)) % modulus

        keys = []
        for i in range(9):
            round_keys = sub_keys[6 * i: 6 * (i + 1)]
            keys.append(tuple(round_keys))
        self._keys = tuple(keys)

    def encrypt(self):
        """
        :return: encrypt with key
        """

        assert 0 <= self.plain < (1 << 64)
        x1 = (self.plain >> 48) & 0xFFFF
        x2 = (self.plain >> 32) & 0xFFFF
        x3 = (self.plain >> 16) & 0xFFFF
        x4 = self.plain & 0xFFFF

        for i in range(8):
            round_keys = self._keys[i]

            y1, y2, y3, y4 = self._ka_layer(x1, x2, x3, x4, round_keys)
            x1, x2, x3, x4 = self._ma_layer(y1, y2, y3, y4, round_keys)

            x2, x3 = x3, x2

        # Note: The words x2 and x3 are not permuted in the last round
        # So here we use x1, x3, x2, x4 as input instead of x1, x2, x3, x4
        # in order to cancel the last permutation x2, x3 = x3, x2
        y1, y2, y3, y4 = self._ka_layer(x1, x3, x2, x4, self._keys[8])

        cipher_text = (y1 << 48) | (y2 << 32) | (y3 << 16) | y4
        return cipher_text


class CAST128(object):
    """ CAST 128 hash """

    def __init__(self, string, key):
        object.__init__(self)
        self.plain = string
        self.key = key
        self.answer = None

    def encrypt(self):
        """
        :return: str
            Encrypt
        """

        iv = Random.new().read(CAST.block_size)
        cipher = CAST.new(self.key, CAST.MODE_OPENPGP, iv)
        self.answer = cipher.encrypt(self.plain)
        return self.answer

    def decrypt(self):
        """
        :return: str
            Decrypt
        """

        eiv = self.plain[:CAST.block_size + 2]
        cipher_text = self.plain[CAST.block_size + 2:]
        cipher = CAST.new(self.key, CAST.MODE_OPENPGP, eiv)
        self.answer = cipher.decrypt(cipher_text)
        return self.answer


class Dsa(object):
    """ dsa hash """

    def __init__(self, string):
        object.__init__(self)
        self.plain = string
        self.hashed = None

    def hash(self):
        """
        :return: hash plaintext
        """

        key = DSA.generate(1024)
        sha1 = SHA(self.plain)
        sha1.hash()
        k = random.StrongRandom().randint(1, key.q - 1)
        self.hashed = key.sign(sha1.hashed, k)
        return self.hashed
