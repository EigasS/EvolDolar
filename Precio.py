import requests
from lxml import html
from datetime import date
import sqlite3

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


conexion = sqlite3.connect("MiBaseSQL.db")
cursor = conexion.cursor()

conexion.execute('''INSERT INTO Cotizaciones (ID, FECHA, DOLAR_BLUE, DOLAR_OFICIAL) values(1,fecha_hoy, precio_usd, precio_usdof)''')

print("ok")

conexion.commit()
conexion.close()