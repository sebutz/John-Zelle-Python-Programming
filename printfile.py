# printfile.py
# prints a file to the screen

def main():
    fname = input("Enter a filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)

main()
