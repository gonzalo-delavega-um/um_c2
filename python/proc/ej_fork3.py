#!/usr/bin/python

from os import fork

def main():
    numero = 1
    if fork() == 0:
        numero += 1
        print("Numero en el hijo tiene %d" % numero)
    else:
        numero -= 1
        print("Numero enel padre tiene %d" % numero)


if __name__ == "__main__":
    main()
