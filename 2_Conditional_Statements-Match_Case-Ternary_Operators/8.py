# 8. A hospital ward has an age restriction. Given patient_age, write an if/else block that sets admission_allowed = True only if the age is exactly 18 or older.

patient_age = int(input('Enter patient age: '))

admission_allowed = True if patient_age >= 18 else False
print(admission_allowed)