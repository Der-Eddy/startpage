import dominate
from dominate.tags import *

doc = dominate.document(title='Startpage', description='Startpage Generator for Webbrowser https://github.com/Der-Eddy/startpage')

with doc.head:
    link(rel='stylesheet', href='style.css')

with doc:
    h1('Startpage ...')

    with div():
        attr(cls='body')
        p('Lorem ipsum..')

print(doc)
with open('index.html', 'w') as file:
    file.write(str(doc))
