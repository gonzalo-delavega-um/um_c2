#!/usr/bin/python

from os import fork

def main():
    if fork() == 0:
        print("Hola desde el hijo!")
    else:
        print("Hola desde el padre!")


if __name__ == "__main__":
    main()
