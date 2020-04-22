# goal: download all the book chapters of "The Making of Jane Austen" from this link
# https://muse.jhu.edu/book/51997

# import requests
from bs4 import BeautifulSoup
import urllib.request

# specify url of webpage with desired links
book_page = 'https://muse.jhu.edu/book/51997'
book_file = 'bookpage_html.html'

# get the html of the page -- DID NOT WORK BECAUSE 503 ERROR FROM REQUESTS
# page = requests.get(book_page)

# parse the html
soup = BeautifulSoup(open(book_file, encoding='utf8'), "html.parser")

# find all a tags
href_tags = []
for a in soup.find_all('a', href=True):
    href = a['href']
    if '/chapter/' and 'pdf' in href:
        href_tags.append(href)

# create list of pdf urls to download
# /chapter/1977239/pdf
pdf_urls = []
for h in href_tags:
    pdf_urls.append('https://muse.jhu.edu' + h)

# use urllib because requests library kept giving 503 error
counter = 1
for p in pdf_urls:
    urllib.request.urlretrieve(p, 'book_pdfs/TheMakingOfJaneAusten' + str(counter) + '.pdf')
    counter += 1
