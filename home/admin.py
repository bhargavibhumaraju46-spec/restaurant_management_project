from bs4 import BeautifulSoup
html_doc = """
<html>
<body>
<img src="restaurant_logo.png">
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
img_tag = soup.find('img')
if img_tag:
    img_tag['alt'] = "delicious Italian restaurant logo with a chef's hat and pasta."
    print(soup.prettify())