# 17. You need to connect to a database. You have a variable server_running. Use short-circuit evaluation to execute a function call connect_database() only if server_running is True, without using any if statements.

def connect_database():
    pass


server_running = True

# Explain me how this works
print(server_running > 0 and connect_database())