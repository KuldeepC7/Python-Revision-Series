# 6. You are checking the health status of a cloud-native Heroku deployment. The server_status variable can be "GREEN", "YELLOW", or "RED". Write a basic match/case block to assign an action string: "All good" for GREEN, "Check logs" for YELLOW, and "Restart Dyno" for RED.

server_status = 'RED'
action = ''

match server_status:
    case 'GREEN':
        action = "All good"
    
    case 'YELLOW':
        action = 'Check logs'
    
    case 'RED':
        action = 'Restart Dyno'


print(action)