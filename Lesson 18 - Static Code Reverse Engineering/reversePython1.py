#!/usr/bin/python

import sys
import base64
import codecs
import math

def main():
    if len(sys.argv) != 4:
        print("Force Quitting")
        return

    classroom = int(sys.argv[1]) 
    cuisine = sys.argv[2] 
    cut = int(sys.argv[3]) 


    result = base64.b64decode("bWFyaW9waXp6YQ==")
    result=str(result,'utf-8')

              
    if ((classroom % 17) == 5) and (result == cuisine) and ((100 // cut) == 4):
        print("correct")
    else:
        print("incorrect")


if __name__ == "__main__":
  main()
