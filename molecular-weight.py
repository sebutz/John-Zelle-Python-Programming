# molecular-weight.py
# A program to calculate molecular weight of carbohydrate based
# on the number of hydrogen, carbon and oxygen atoms in the molecule.

def main():
    print("This program is used to compute molecular weight.")

    hydrogen_weight = 1.00794
    carbon_weight = 12.0107
    oxygen_weight = 15.9994

    hydrogen_molecule = float(input("Please enter the number of hydrogen atoms: "))
    carbon_molecule = float(input("Please enter the number of carbon atoms: "))
    oxygen_molecule = float(input("Please enter the number of oxygen atoms: "))

    print("Calculating...")

    molecular_weight = hydrogen_weight * hydrogen_molecule + carbon_weight * carbon_molecule + oxygen_weight * oxygen_molecule

    print("The molecular weight of the entered carbohydrate is", molecular_weight, "grams/mole.")

main()
