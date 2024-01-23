# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:53:50 2019

@author: Mary
"""
#ESTRAZIONE TESTO DALLE PAGINE ESTRATTE IN BASE AI NODI ESTRATTI
import csv
import requests
from bs4 import BeautifulSoup

file_csv = 'www.kikocosmetics.com.csv'
with open(file_csv,newline='') as csvfile:
    reader = csv.reader(csvfile,delimiter = ' ')  
    for row in reader:
        print (row[0])
        page = requests.get(row[0])
        data = page.text
        soup = BeautifulSoup(data)
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        
        # get text
        text = soup.get_text()
        
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        print(text)
        file = open('testo_paginaweb5.txt','a')
        file.write(str(text))
        file.close()
                        
