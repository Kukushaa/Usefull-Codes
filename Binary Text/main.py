from binary import *

def Binary(text):
    Alphabete = list(text)
    tmp = text

    for i in Alphabete:
        if 'A' in Alphabete:
            copy = tmp.replace('A', BigAlph[0])
            tmp = copy

        if 'B' in Alphabete:
            copy = tmp.replace('B', BigAlph[1])
            tmp = copy

        if 'C' in Alphabete:
            copy = tmp.replace('C', BigAlph[2])
            tmp = copy

        if 'D' in Alphabete:
            copy = tmp.replace('D', BigAlph[3])
            tmp = copy

        if 'E' in Alphabete:
            copy = tmp.replace('E', BigAlph[4])
            tmp = copy

        if 'F' in Alphabete:
            copy = tmp.replace('F', BigAlph[5])
            tmp = copy

        if 'G' in Alphabete:
            copy = tmp.replace('G', BigAlph[6])
            tmp = copy

        if 'H' in Alphabete:
            copy = tmp.replace('H', BigAlph[7])
            tmp = copy

        if 'I' in Alphabete:
            copy = tmp.replace('I', BigAlph[8])
            tmp = copy

        if 'J' in Alphabete:
            copy = tmp.replace('J', BigAlph[9])
            tmp = copy

        if 'K' in Alphabete:
            copy = tmp.replace('K', BigAlph[10])
            tmp = copy

        if 'L' in Alphabete:
            copy = tmp.replace('L', BigAlph[11])
            tmp = copy

        if 'M' in Alphabete:
            copy = tmp.replace('M', BigAlph[12])
            tmp = copy

        if 'N' in Alphabete:
            copy = tmp.replace('N', BigAlph[13])
            tmp = copy

        if 'O' in Alphabete:
            copy = tmp.replace('O', BigAlph[14])
            tmp = copy

        if 'P' in Alphabete:
            copy = tmp.replace('P', BigAlph[15])
            tmp = copy

        if 'Q' in Alphabete:
            copy = tmp.replace('Q', BigAlph[16])
            tmp = copy

        if 'R' in Alphabete:
            copy = tmp.replace('R', BigAlph[17])
            tmp = copy

        if 'S' in Alphabete:
            copy = tmp.replace('S', BigAlph[18])
            tmp = copy

        if 'T' in Alphabete:
            copy = tmp.replace('T', BigAlph[19])
            tmp = copy

        if 'U' in Alphabete:
            copy = tmp.replace('U', BigAlph[20])
            tmp = copy

        if 'V' in Alphabete:
            copy = tmp.replace('V', BigAlph[21])
            tmp = copy

        if 'W' in Alphabete:
            copy = tmp.replace('W', BigAlph[22])
            tmp = copy

        if 'X' in Alphabete:
            copy = tmp.replace('X', BigAlph[23])
            tmp = copy

        if 'Y' in Alphabete:
            copy = tmp.replace('Y', BigAlph[24])
            tmp = copy

        if 'Z' in Alphabete:
            copy = tmp.replace('Z', BigAlph[25])
            tmp = copy

        else:
            pass

    #Small
    for j in Alphabete:
        if 'a' in Alphabete:
            copy = tmp.replace('a', SmallAlph[0])
            tmp = copy

        if 'b' in Alphabete:
            copy = tmp.replace('b', SmallAlph[1])
            tmp = copy

        if 'c' in Alphabete:
            copy = tmp.replace('c', SmallAlph[2])
            tmp = copy

        if 'd' in Alphabete:
            copy = tmp.replace('d', SmallAlph[3])
            tmp = copy

        if 'e' in Alphabete:
            copy = tmp.replace('e', SmallAlph[4])
            tmp = copy

        if 'f' in Alphabete:
            copy = tmp.replace('f', SmallAlph[5])
            tmp = copy

        if 'g' in Alphabete:
            copy = tmp.replace('g', SmallAlph[6])
            tmp = copy

        if 'h' in Alphabete:
            copy = tmp.replace('h', SmallAlph[7])
            tmp = copy

        if 'i' in Alphabete:
            copy = tmp.replace('i', SmallAlph[8])
            tmp = copy

        if 'j' in Alphabete:
            copy = tmp.replace('j', SmallAlph[9])
            tmp = copy

        if 'k' in Alphabete:
            copy = tmp.replace('k', SmallAlph[10])
            tmp = copy

        if 'l' in Alphabete:
            copy = tmp.replace('l', SmallAlph[11])
            tmp = copy

        if 'm' in Alphabete:
            copy = tmp.replace('m', SmallAlph[12])
            tmp = copy

        if 'n' in Alphabete:
            copy = tmp.replace('n', SmallAlph[13])
            tmp = copy

        if 'o' in Alphabete:
            copy = tmp.replace('o', SmallAlph[14])
            tmp = copy

        if 'p' in Alphabete:
            copy = tmp.replace('p', SmallAlph[15])
            tmp = copy

        if 'q' in Alphabete:
            copy = tmp.replace('q', SmallAlph[16])
            tmp = copy

        if 'r' in Alphabete:
            copy = tmp.replace('r', SmallAlph[17])
            tmp = copy

        if 's' in Alphabete:
            copy = tmp.replace('s', SmallAlph[18])
            tmp = copy

        if 't' in Alphabete:
            copy = tmp.replace('t', SmallAlph[19])
            tmp = copy

        if 'u' in Alphabete:
            copy = tmp.replace('u', SmallAlph[20])
            tmp = copy

        if 'v' in Alphabete:
            copy = tmp.replace('v', SmallAlph[21])
            tmp = copy

        if 'w' in Alphabete:
            copy = tmp.replace('w', SmallAlph[22])
            tmp = copy

        if 'x' in Alphabete:
            copy = tmp.replace('x', SmallAlph[23])
            tmp = copy

        if 'y' in Alphabete:
            copy = tmp.replace('y', SmallAlph[24])
            tmp = copy

        if 'z' in Alphabete:
            copy = tmp.replace('z', SmallAlph[25])
            tmp = copy

        else:
            pass

    print(copy)

    return text

def main():
    text = input("Enter your text: ")
    Binary(text)

if __name__ == '__main__':
    main()