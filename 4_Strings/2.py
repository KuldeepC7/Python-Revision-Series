# 2. A patient's blood pressure data from legacy medical hardware at Kataria Multispecialist Hospital arrives with messy whitespace: `"  120/80 \n"`. Use the `.strip()` method to clean it and store it in a new variable.

patient_blood_pressure = '     120/80  \n'
clean_patient_data = patient_blood_pressure.strip()
print(clean_patient_data)