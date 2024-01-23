# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:52:56 2019

@author: Mary
"""

from bs4 import BeautifulSoup #per l'estrazione dei link
import requests
import re
import networkx as nx #per i grafi
from random import choice #estrazione random
import csv


#APERTURA DI LINK 
#driver=webdriver.Chrome()
#driver.get("https://www.alfaromeo.it/")

#estrazione dei link dalla pagina web
url = "https://www.alfaromeo.it/"
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data,"html.parser")

#GRAFO RETE 
FielName="graph_cb.txt"#file che contiene la rete
Graph=nx.DiGraph()
G=nx.read_edgelist(FielName,create_using=Graph, nodetype=int, data=(('weight',float),))
num_nodi=len(G)
print("numero di nodi: ",num_nodi)
archi=G.edges()
print("numero di archi: ", len(archi))
#nodi figli G.degree(x)
i=range(1,6)
somma=0
for j in i:

    #print(j,":")
    random_node = choice(list(G.nodes))#estraggo random un nodo della rete
    #print("Nodo: ",random_node, "figli: ",G.degree(random_node))
    figli=G.degree(random_node)
    somma=somma+figli
    if(j==1):
        x=0
        y=figli+x
        k=y
        #print("DA",x, "a", y)
    else:
        x=k+1
        y=figli+x
        #print("DA",x, "a", y)
        
    #NAVIGAZIONE TRA I LINK 
    links = []#lista di link 
    for link in soup.find_all(attrs={'href': re.compile("http")}):
        links.append(link.get('href'))#estrazione
    lung_link=len(links)#link contenuti nel file
    #print("lung ", len(links))
    
        
    #controllo finchè il numero di link contenuto nella pag. è sufficiente
    #per ciascun nodo, se i nodi sono stati distribuiti
    while lung_link<figli:
        break
    else: figli=G.degree(random_node)
    while somma>lung_link:
        break
    else:figli =figli=G.degree(random_node)

    
    if (lung_link>figli):
        if (somma<lung_link):
            print("Nodo: ",random_node, "figli: ",G.degree(random_node))
            #print("somma ", somma)
            nodi=[]
            nodi="Nodo: ",random_node, "figli: ",G.degree(random_node)
            file = open('NODI_ESTRATTI.txt','a')
            file.write(str(nodi))
            file.close()
            lista=[]
            lista=links[x:figli+x]
            print(lista)
            
            file = open('prova.txt','a')
            file.write(str(lista))
            file.close()
            
            
            with open('prova.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(lista)
            
           
                
          
    k=y
if(somma<lung_link) :
    random_node = choice(list(G.nodes))
    if(G.degree(random_node)<somma):
        print("Nodo: ",random_node, "figli: ",G.degree(random_node))
        #print("somma ", somma)
        lista=[]
        lista=links[x:figli+x]
        print(lista)


#STAMPO VALORE PERCENTUALE DEI NODI VISITATI
print("NODI visitati: ",len(i))        
perc=(100/num_nodi)*len(i)
print("percentuale visitata: ",perc)
