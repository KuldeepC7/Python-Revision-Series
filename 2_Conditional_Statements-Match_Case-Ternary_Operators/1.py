# 1. You are writing the triage logic for a hospital management system. Given a variable patient_temperature, write an if/elif/else block that assigns a status variable to "Critical" if the temperature is above 103.0, "Fever" if it's above 99.5, and "Normal" otherwise.

patient_temperature = 105.0
pateint_status = ''

if patient_temperature >= 103.0:
    pateint_status = 'Critical'

elif patient_temperature >= 99.5:
    pateint_status = 'Fever'

else:
    pateint_status = 'Normal'

print(pateint_status)