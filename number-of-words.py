# number-of-words.py
# a program to calculate the number of words in a sentence

def main():

    input_sentence = input("Please enter a sentence: ")

    list = []

    for i in input_sentence.split():
        list.append(i)
    print(len(list))
main()
