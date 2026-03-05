# 9. An external API returns an HTTP status code as an integer (200, 400, 404, or 500). Write a match/case block that assigns a string response_message based on these exact numbers, and use the wildcard case (_) to assign "Unknown Error" for any other number.

status_code = int(input('Enter status coce: '))
response_message = ''

match status_code:
    case 200:
        response_message = 'success'
    
    case 400: 
        response_message = 'Bad Rquest'

    case 404:
        response_message = 'page not found'

    case 500:
        response_message = 'Internal Server Error'
    
    case _:
        response_message = 'Unknown Error'
    
print(response_message)