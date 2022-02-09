import requests
from bs4 import BeautifulSoup

'''
res = requests.get("http://www.sportsseoul.com/news/read/1017460/")

print(res.content)

soup = BeautifulSoup(res.content, 'html.parser')

title = soup.find('title')

print(title.get_text())
'''

html = """
<html> 
    <body>
        <h1 id='title'>[1]crawling ways</h1>;
        <p class='cssstyle'>webpage crawler</p>
        <p id='body' align = 'center'>python oriented crawler </p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
title_data = []
title_data = soup.find_all('p')

print(title_data)
print(title_data[0].string)
print(title_data[1].get_text())

soup_2 = BeautifulSoup(html, 'html.parser')
text_data = soup.find( 'p', attrs = {'align':'center'})

print(text_data.string)