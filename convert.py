# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computwell

# def main():
#    print("This program is used to convert Celsius to Fahrenheit.")
#    celsius = eval(input("WHat is the Celsius temperature? "))
#    fahrenheit = 9/5 * celsius + 32
#    print("The temperature is", fahrenheit, "degrees Fahrenheit")

# main()

'''
def main():

    print("This program is used to convert Celsius to Fahrenheit.")

    for i in range(5):
        celsius = eval(input("WHat is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahreneheit")

main()
'''
'''
def main():
    print("This program prints a table of Celsius values mapped to Fahrenheit from 0 do 100 degrees.")
    print("C:  ||  F:")
    celsius = 0
    for i in range(11):
        fahrenheit = 9/5 * celsius + 32
        print(celsius, " || ", fahrenheit)
        celsius = celsius + 10
main()
'''

def another_main():
    print("This program is used to convert Fahrenheit to Celsius.")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) / (9 / 5)
    print("The temperature is", celsius, "degrees in Celsius")

another_main()
