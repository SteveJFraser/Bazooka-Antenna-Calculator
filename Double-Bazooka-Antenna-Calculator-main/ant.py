"""
BAZOOKA DIPOLE ANTENNA CALCULATOR
---------------------------------------------------------
This program takes in a frequency
and calculates the length of a Double Bazooka Antenna (coaxial dipole)
then creates a txt file and writes the results to the file
"""


def clear_screen():
    print("\n" * 50)


clear_screen()
print("--DOUBLE BAZOOKA ANTENNA--\n___________________________")
freq = float(input("Enter the Antenna Frequency: "))
formula_total = 299.792458 / freq * 0.9993 * 0.50
formula_centre = 299.792458 / freq * 0.6595 * 0.50
end = (formula_total - formula_centre) / 2
final_result = f"""             
               Your Coaxial Dipole Length In Metres
                    (Frequency = {freq} MHz)
                         Total Length
          |------------------{formula_total:.3f}------------------|
          -----------==========-==========-----------    
                         Braid Length
                    |--------{formula_centre:.3f}--------|         
          -----------==========-==========-----------
          |--{end:.3f}--|          |--------{formula_total/2:.3f}--------|
          End Length                  Half Length"""
clear_screen()
with open("bazooka.txt", "w") as write_to_file:
    write_to_file.write(final_result)
print(final_result)
print("\n"*3)
