# numbers2text.py
# A program to convert a sequence of Unicode numbers into
#   a string of text.

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # loop through each substring and build Unicode message

    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)               # converts digits to a number
        message = message + chr(codeNum)    # concatentate character to message

    print("\nThe encoded message is: ", message)

main()
