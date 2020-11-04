import re

prev_page_url = "/ru/flows/develop/page1/"

prev_page_url = re.sub(r'page\d+', 'page100', prev_page_url)

print(prev_page_url)
