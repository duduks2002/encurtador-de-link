#feito por Edward Abromovik para fins didaticos

import pyshorteners

url = 'colocar link aqui'
link = pyshorteners.Shortener()
shorten_url = link.tinyurl.short(url)
print(f'\n{shorten_url}')