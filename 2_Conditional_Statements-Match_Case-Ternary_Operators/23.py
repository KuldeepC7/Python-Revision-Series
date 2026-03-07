# 23. Combine a ternary operator with short-circuiting for an on-call system. Assign a final_doctor variable: it should be primary_doctor if primary_available is True, otherwise backup_doctor if backup_available is True, and if neither are available, default to the string "Emergency Ward". Write this in a single line.

primary_available = False
backup_available = False

final_doctor = 'primary_doctor' if primary_available else('backup_doctor' if backup_available else 'Emergency Ward')
print(final_doctor)