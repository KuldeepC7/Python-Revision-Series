# 6. In a music production script, a beat drops every 16 bars. Given a variable current_bar, write an expression using the modulo operator to evaluate to 0 whenever a beat should drop.

current_bar = 48

will_drop = (current_bar % 16 == 0)

print(will_drop)