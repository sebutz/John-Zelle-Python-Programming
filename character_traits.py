# character-traits.py
# a program to determine character traits from input name

def main():

    input_name = input("Please enter your name: ")

    list = [" ","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]

    character_trait = 0

    for i in input_name.lower():
        number = list.index(i)
        character_trait = character_trait + number
    print(character_trait)
main()
