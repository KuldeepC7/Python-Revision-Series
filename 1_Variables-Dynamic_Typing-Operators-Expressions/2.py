#2. For an e-commerce website with a "Desi-Earth" theme, you need a default hex color code.
#Assign the string "#8B5A2B" to three separate variables (primary_color, button_color, footer_color) in a single line.
#Then, write an expression to check if primary_color and button_color point to the exact same memory location.


primary_color = button_color = footer_color = "#8B5A2B"

print(id(primary_color)) #1518769604144
print(id(button_color))#2093971932720 2093971932720

print(id(primary_color) == id(button_color))
