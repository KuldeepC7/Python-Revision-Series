# 4. A customer searches for a product on your Hooka and Ghosa site: `"   Dung Cakes   "`. Chain the `.strip()` and `.lower()` methods together in a single line to normalize this search query to `"dung cakes"`.

product_search_query = '       Dung Cakes            '
modified_query = product_search_query.strip().lower()
print(modified_query)