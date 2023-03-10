import sys

# get arguments
if len(sys.argv) != 2:
    print("Usage: python3 sys_example.py <NAME>")
    quit()

name = sys.argv[1]

print("Nice to meet you,",name)