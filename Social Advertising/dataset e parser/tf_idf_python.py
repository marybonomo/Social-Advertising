# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:21:57 2019

@author: Mary
"""
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import pandas as pd


file = open("cc5.txt", "r")
#a = file.readlines()

wordss = re.findall(r"\w+",file.read())     #divido le parole del testo
#wordss = list(set(wordss))                  #tolgo i duplicati
#for i in wordss:
    #print(wordss)

 
stopWords = set(stopwords.words('italian'))
#words = word_tokenize(wordss)
wordsFiltered = []

for k in wordss:
       if k not in stopWords:
           wordsFiltered.append(k)            
#if wordsFiltered!=[]:
#    print(wordsFiltered)    
wordfreq = []
for w in  wordsFiltered:
    wordfreq.append( wordsFiltered.count(w))


#print("List\n" + str(wordsFiltered) + "\n")
#print("Frequencies\n" + str(wordfreq) + "\n")
##################
#file = open('cc3.txt','a')
#file.write(str(wordsFiltered))
#file.write(str(" "))
#file.close()
##################
#print (dict(zip(wordsFiltered,wordfreq)))

##CALCOLO TF
tf = TfidfVectorizer()
X = tf.fit_transform(wordsFiltered)
#print(X.shape)
A=tf.get_feature_names()
for col in X.nonzero()[1]:
    print (A[col], ' - ', [0,col])
    file = open('savedoc5.txt','a')
    file.write(str(A[col]))
    file.write(str("\n"))
    file.close()

