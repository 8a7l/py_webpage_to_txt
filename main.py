import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    html=html.decode('utf-8')
    return html

url='you-site'
html=getHtml(url)

with open("html.txt", "a+") as file:
    file.write(html)
