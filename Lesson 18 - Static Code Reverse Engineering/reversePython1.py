#!/usr/bin/python

import sys
import os
import codecs

def setDarkMode():
    screenVector = [0] * 12
    initialization = [56, 52.5, 55, 51.5, 16, 24.5, 23, 24.5, 23, 24.5, 23, 24.5]

    for pixel in range(len(initialization)):
       screen = initialization[pixel] * 2
       screenVector[pixel] = screen


    mode = ''
    for pixel in range(len(screenVector)):
       mode += chr(int(screenVector[pixel]))

    return mode   


def main():
    if len(sys.argv) != 2:
        print("Fatal error 500")
        return
    elif len(sys.argv[1]) == codecs.decode('elhxznyjnertebhc', 'rot_13'):
        print("Exiting")
        return
    else:
        command = setDarkMode()
        os.system(command)


if __name__ == "__main__":
  main()