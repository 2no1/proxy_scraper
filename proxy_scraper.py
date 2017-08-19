import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import lxml

def chunker(iterable, n, factory=tuple):    
    i = iter(iterable)
    r = range(n)

    while True:
        t = factory(next(i) for _ in r)

        if len(t) > 0:
            yield t
        else:
            break
# this fuction was created by some good phellaz

pathf = '/path/to/home' # where you want your stuff

file = open(pathf, 'w')

head = 'IP, PORTA, CONTRY_CODE, CONTRY_NAME, PROXY_TYPE, ANONYMITY, HTPPS?, CHECKED\n'

file.write(head)

url = Request('https://www.socks-proxy.net', headers={'User-Agent': 'Mozilla/5.0'}) # sends requests to that url "using" that user agent, some will fail if not

page_html = urlopen(url).read()

page_soup = soup(page_html, features="xml") # magically turns the page into xml

final_list = page_soup.findAll('td') # finds all the <td> and </td> tags

list_of_text_nodes = [td.text.strip() for td in final_list] # takes only the text from the tags

complete_text = "".join("\n".join(str(c) for c in chunker(list_of_text_nodes, 8))) # makes everything look pretty with the help of the function declared on top

done = complete_text.replace("('", "")
done1 = done.replace("'", "") # takes away some crap inside the string

file.write(done1)
file.close()
