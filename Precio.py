import requests
from lxml import html
from datetime import date

url2 = 'https://dolarhoy.com/'
page2 = requests.get(url2)

tree2 = html.fromstring(page2.content)

USD = tree2.xpath('//*[@id="home_0"]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/text()')
precio_usd = (USD[0]).strip('$')
USDO = tree2.xpath('//*[@id="home_0"]/div[2]/section/div/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/text()')
precio_usdof = ((USDO[0]).strip('$'))

fecha_hoy = date.today()
fecha_hoy = str(fecha_hoy)

print (precio_usd)
print (precio_usdof)

archivo = open("Precios2.txt","a")
archivo.write(fecha_hoy+';'+'0000'+';'+'0000'+';'+precio_usd+';'+precio_usdof+"\n")
archivo.close()

