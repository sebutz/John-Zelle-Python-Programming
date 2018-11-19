# gregorican-epact.py
# A program to calculate the date of Easer from the year that is provided by the user

def main():
    year = int(input("Please enter the current year: "))

    C = year // 100

    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 *(year % 19))%30

    print("The epact is", epact)

main()
