print("Enter 3 isotopes here: ")
isotope1 = float(input("Isotope 1: "))
isotope2 = float(input("Isotope 2: "))
isotope3 = float(input("Isotope 3: "))

print("Enter abundance in decimal form for each isotope below: ")
abundance1 = float(input("Abundance 1: "))
abundance2 = float(input("Abundance 2: "))
abundance3 = float(input("Abundance 3: "))

atomicmass = float(abundance1) * float(isotope1) + float(abundance2) * float(isotope2) + float(abundance3) * float(isotope3)
print("The Average Atomic Mass is...", atomicmass)
