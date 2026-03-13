# 8. You have a tuple of command arguments in Manjaro Linux: `("sudo", "systemctl", "restart", "nginx")`. Use the `.join()` method with a space separator `" "` to combine them into a single executable string command.

command_arguments = ('sudo', 'systemctl', 'restart', 'nginx')
single_executable_command = ' '.join(command_arguments)

print(single_executable_command)