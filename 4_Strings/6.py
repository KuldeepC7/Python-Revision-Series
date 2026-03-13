# 6. You have a comma-separated string of TCS Ignite exam centers: `"Indore,Bhopal,Gwalior"`. Use `.split(",")` to break this string apart, and write a `for` loop to print each city on a new line.

TCS_ignite_exam_centres = 'Indore,Bhopal,Gwalior'

for center in TCS_ignite_exam_centres.split(','):
    print(center)