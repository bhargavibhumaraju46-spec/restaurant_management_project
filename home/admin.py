from bs4 import BeautifulSoup
html = """
"""
soup = BeautifulSoup(html, 'html.parser')
terms_link = soup.new_tag('a', href='/terms-of-service', text='Terms of Service')
separator = soup.new_string('|')
footer_p = soup.find('p')
footer_p.append(separator)
footer_p.append(terms_link)
print(soup.prettify())
                               