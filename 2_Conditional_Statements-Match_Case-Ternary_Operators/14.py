# 14. Write a nested ternary operator for a system logger. Assign log_level to "DEBUG" if environment == "dev", "INFO" if environment == "prod", and "WARN" for anything else.

# system logger

environment = input('What is environment type: ')

log_level = 'DEBUG' if environment == 'dev' else('INFO' if environment == 'prod' else 'WARN')

print(log_level)
