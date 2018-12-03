# acronym.py
# a program to create an acronym from the input phrase

def main():

    input_string = input("Please enter the input string: ")

    list = []
    for i in input_string.split():
        list.append(i)

    acronym = ""

    for j in list:
        acronym = acronym + j[0]

    print(acronym.upper())
main()
