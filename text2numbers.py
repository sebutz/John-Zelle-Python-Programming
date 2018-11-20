# text2numbers.py
# A program to convert textual message into a sequence of
#   numbers, utilizing the underlying Unicode encoding.

def main():

    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")

    # get the message to encode
    message = input("Please enter the message to Encode: ")

    print("\nHere are the Unicode codes: ")

    # loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end="")

    print()

main()
