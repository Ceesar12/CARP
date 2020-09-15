import requests
import os
import sys
from bs4 import BeautifulSoup as bs
import webbrowser
#César Alejandro Rodríguez Pérez - 1734223
#Como tal, lo que se busca en el script es buscar una pagina de la UANL
#Dando como parametros de busqueda un número incial y un número final
#Y pidiendo las siglas de la facultad para buscar la pagina almacenada
#en dicha pagina de dicha faultad. En dado caso que no se encuentre
#Mostrara un mensaje de error que dice "Pagina no encontrada".
print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
    

