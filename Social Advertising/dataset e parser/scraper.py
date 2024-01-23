# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 17:02:30 2019
@author: Mary
"""

import bs4
import requests
import urllib
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import csv
from datetime import datetime

#PER ESTRARRE HTML
def estrapola_sorgente(url):
    if 'http://' in url:
        sorgente = requests.get(url).text
        print(sorgente)
        return(sorgente)
    else:
        return("L'url non è valido")

#PER ESTRARRE H1 DA HTML
def estrapola_h1(sorgente):
    soup = bs4.BeautifulSoup(sorgente)
    elenco = soup.findAll('h1')
    if elenco:
        for a in elenco:
            print(a)
    else:
        print("Non ci sono H1 in questa pagina")

#PER ESTRARRE I LINK 
def estrapola_nofollow(sorgente):
    soup = bs4.BeautifulSoup(sorgente)
    elenco = soup.find_all('a')
    contatore = 0
    if elenco:
        for a in elenco:
            if a.get('rel'):
                if 'nofollow' in a.get('rel')[0]:
                    contatore += 1
                    print(a.get('href'))
        if contatore == 0:
            print("Non ci sono link con il nofollow")
    else:
        print("Non ci sono link in questa pagina")



#ESTRAI HTML PAGINA WEB
#response = urllib.request.urlopen("https://www.alfaromeo.it/")
#pagina = response.read()
#response = requests.get("https://www.alfaromeo.it/")
#pagina = response.text
#print(pagina)


#ESTRAZIONE LINK DALLA PAGINA
url = "https://www.alfaromeo.it/"
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data)

for link in soup.find_all("a"):
    print(link.get("href"))

#PER ESTRARRE TESTO
#url = "https://www.alfaromeo.it/"
#con = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(con,'html.parser')
#texts = soup.get_text()
#print(texts)

#estrapola_sorgente('http://www.danilopetrozzi.it')
#lista_siti = [
#    'https://www.alfaromeo.it/',
#    'blog.giallozafferano.it/',
#    'https://www.carpisa.it/it_it/',
#    'https://www.fedezofficial.com/',
#    'https://www.kikocosmetics.com/it-it/',
#    ]

#for sito in lista_siti:
#    sorgente = estrapola_sorgente(sito)
#    print(sito)
    #estrapola_h1(sorgente)
    #estrapola_nofollow(sorgente)
    #print()

