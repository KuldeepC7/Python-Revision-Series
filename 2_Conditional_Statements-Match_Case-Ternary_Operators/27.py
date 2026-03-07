# 27. A payment gateway returns varying tuple structures: ("SUCCESS", transaction_id) or ("FAILED", error_code, retry_allowed_boolean). Write a match/case block that handles both. For the failed case, extract the boolean and use a nested if to determine if the system should re-queue the payment.


p_g_r_str = input('Enter tuple elements with comma between them in single line: ')

p_g_r_tuple = tuple(p_g_r_str.split(','))

if len(p_g_r_tuple) < 3:
    payment_gateway_returns = (p_g_r_tuple[0], int(p_g_r_tuple[1]))

else:
    payment_gateway_returns = (p_g_r_tuple[0], int(p_g_r_tuple[1]), eval(p_g_r_tuple[2]))



match payment_gateway_returns:
    case (response_message, transaction_id):
        print('Success', transaction_id)
    
    case (response_message, error_code, retry_allowed_boolean):
        if retry_allowed_boolean:
            print('re-queue: The transaction is in queue again')
        
        else:
            print('Retry')
    
    case _:
        print('Malformed tuple')