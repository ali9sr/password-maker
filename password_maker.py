import string
import argparse
from random import choices


def pass_maker(length=8, uppercase=False, lowercase=False, digits=False, pun=False):
    p = ''

    if uppercase:
        p += string.ascii_uppercase

    if lowercase:
        p += string.ascii_lowercase

    if digits:
        p += string.digits

    if pun:
        p += string.punctuation

    if p == '':
        p += string.ascii_letters

    return ''.join(choices(p, k=length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='a strong password maker (T.me/aliwin1)')
    parser.add_argument('length', type=int, help='password length')
    parser.add_argument('-u', '--uppercase', help='use uppercase', action='store_true')
    parser.add_argument('-l', '--lowercase', help='use lowercase', action='store_true')
    parser.add_argument('-d', '--digits', help='use digits', action='store_true')
    parser.add_argument('-p', '--punctuation', help='use punctuation', action='store_true')
    args = parser.parse_args()

    print(pass_maker(args.length, args.uppercase, args.lowercase, args.digits, args.punctuation))
