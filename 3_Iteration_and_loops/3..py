# 3. A Hospital Management System needs to record the temperatures of exactly 3 patients. Write a for loop that uses the input() function three times to ask for a temperature, and prints "Recorded" after each entry.

for patient in range(1, 4):
    temperature = float(input(f"Enter temperature for patient {patient}: "))
    print(f"Temperature recorded for patient {patient}: {temperature}")