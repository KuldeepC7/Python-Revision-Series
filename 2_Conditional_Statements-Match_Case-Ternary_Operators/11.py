# 11. An incoming hospital record is represented as a tuple: record = ("symptom", severity_level). For example, ("chest_pain", 8). Write a match/case block that unpacks this tuple. If the symptom is "chest_pain", assign priority 1. If "fever", assign priority 2. Otherwise, assign priority 3.

priority = 0
record = ("Pain in hands", 2)

symptom, severity_level = record

match symptom:
    case "chest pain":
        priority = 1
    
    case "fever":
        priority = 2
    
    case _:
        priority = 3

print(priority)