# 15. An SMS gateway integration strictly requires messages to be under 160 characters. Given `sms_body = "Your ride is confirmed..."`, write an `if/else` block using an f-string to print "Sent" if valid, or "Failed: Length is {length}" if it exceeds the limit.

sms_body = "Your ride is confirmed....."

if len(sms_body) <= 160:
    print('Sent')
else:
    print(f'Failed: Length is {len(sms_body)}')