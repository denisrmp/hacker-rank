# https://www.hackerrank.com/challenges/caesar-cipher-1


alpha_max = ord('z') - ord('a') + 1


def round_char(c, rounds, limit):
    c = ord(c) + rounds
    if c > ord(limit):
        return chr(c - alpha_max)
    else:
        return chr(c)


def cipher_char(c, rounds):
    if 'a' <= c <= 'z':
        return round_char(c, rounds, 'z')
    elif 'A' <= c <= 'Z':
        return round_char(c, rounds, 'Z')
    else:
        return c


def caesar_cipher(plain, rounds):
    rounds %= alpha_max  # adjusting rounds to simplify calculation
    return ''.join([cipher_char(c, rounds) for c in plain])


n = int(input())
plain = input()
rounds = int(input())
print(caesar_cipher(plain, rounds))
