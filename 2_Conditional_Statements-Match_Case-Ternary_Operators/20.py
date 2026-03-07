# 20. A script categorizes tech blogs based on a keyword string. Write an if/elif/else block: if the keyword is exactly "solar" or "wind", category is "Renewable". If "battery", category is "Storage". Else, "General".

keyword_in_blog = input('What is keyword: ')
category = None

if keyword_in_blog == 'solar' or keyword_in_blog == 'wind':
    category = 'Renewable'

elif keyword_in_blog == 'battery':
    category = 'Storage'

else:
    category = 'General'

print(category)