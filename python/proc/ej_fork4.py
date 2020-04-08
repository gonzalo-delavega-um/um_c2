#!/usr/bin/python

from os import fork

def main():
    fork()
    fork() and fork()

    print("Forkeando!!")


if __name__ == "__main__":
    main()
