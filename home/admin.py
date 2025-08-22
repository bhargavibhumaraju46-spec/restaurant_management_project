from bs4 import BeautifulSoap
html_content = """
<html>
<body>
<img src="example.jpg">
</body>
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')
for img in soup.find_all('img'):
    if not img.get('alt'):
        img['alt'] = 'Descriptive alt textfor accesibility'
print(soup.prettify())
                 
    