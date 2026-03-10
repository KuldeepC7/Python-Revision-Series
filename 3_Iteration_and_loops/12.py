# 12. You have a tuple of patient triage statuses: ("Stable", "Stable", "Critical", "Stable"). Use a for loop to search through them. If "Critical" is found, break and print "Emergency Alert". Use the else clause to print "All patients stable" if no critical status is found.

patient_triage_statuses = ('Stable', 'Stable', 'Critical', 'Stable')

for status in patient_triage_statuses:
    if status == 'Critical':
        print('Emergency Alert')
        break
    
    else:
        print('All patients stable')