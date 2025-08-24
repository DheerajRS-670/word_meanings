import argparse
import sys

lcdict = {
               'a': 1, 'i': 1, 'j': 1, 'q': 1, 'y': 1,
               'b': 2, 'k': 2, 'r': 2,
               'c': 3, 'g': 3, 'l': 3, 's': 3,
               'd': 4, 'm': 4, 't': 4,
               'e': 5, 'h': 5, 'n': 5, 'x': 5,
               'u': 6, 'v': 6, 'w': 6,
               'o': 7, 'z': 7,
               'f': 8, 'p': 8
              }
lndict = {}

for i in range(97, 97+26):
    lndict[chr(i)] = i - 96

chaldean = True

for i in range(0, 10):
    lcdict[str(i)] = i
    lndict[str(i)] = i

def dig_sum(num):
    if num < 10:
        return num

    dsum = 0
    while num != 0:
        digit = num % 10
        dsum += digit
        num = num // 10

    dsum = dig_sum(dsum)    
    return dsum

def char_sum(word):
    total = 0
    for c in word:
        if chaldean:
            total += lcdict[c]
        else:
            total += lndict[c]
            
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", required=False, type=str, help="The word")
    parser.add_argument("-n", "--normal", required=False, action='store_false',
                        help="Use normal dictionary (else Chaldean is used)")
    args = parser.parse_args()

    chaldean = args.normal

    if args.word:
        print(dig_sum(char_sum(args.word)))
        sys.exit(0)

    fd = open('../dict/words', 'r')
    words = fd.read()
    fd.close()

    wlist = [x for x in words.split() if "'" not in x]
    wlist = [x.lower() for x in wlist]
    wlist = [x for x in wlist if x.isascii()]
    
    wdict = {}

    for i in range(1, 10):
        wdict[i] = []

    for word in wlist:
        wdict[dig_sum(char_sum(word))].append(word)

    for key in wdict.keys():
        if chaldean:
            fname = f"../arranged/chaldean/{key}.txt"
        else:
            fname = f"../arranged/normal/{key}.txt"
            
        fd = open(fname, 'w')
        fd.write("\n".join(wdict[key]))
        fd.close()
