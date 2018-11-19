# lightning-distance.py
# A program to determine the distance to a lightning strike
# based on the time elapsed between the flash and the sound of The
# thunder.

def main():
    time = float(input("Please enter the time elapsed after the lightning in seconds: "))

    print("Calculating...")

    distance_in_miles = (time * 1100) / 5280

    distance_in_km = distance_in_miles * 1.60934

    print("The distance of the lightning strike is", distance_in_km, "kilometers.")

main()
