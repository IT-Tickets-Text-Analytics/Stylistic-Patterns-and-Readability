#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import sys

import matplotlib.pyplot as plt
#from nltk.corpus import brown
import matplotlib as mpl
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'
import codecs
import sys, os
import os.path
import nltk
import re
import requests
import numpy
from numpy import *
import nltk
import scipy
from tkinter import Tk
from tkinter.filedialog import *
from tkinter.messagebox import *
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from settings import stem
from nltk.corpus import stopwords
from nltk.stem import  SnowballStemmer

stemmer = SnowballStemmer(stem)

    
def word_count(stopword):
   #path='C:/Users/ninar/OneDrive/Documents/Research/Telecom/Tickets_separated'
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/Texts'
   k=0
   #fb=open('Text.txt', 'wb')
   
   a=sorted(os.listdir(path))
   #path_1='C:/Users/ninar/OneDrive/Documents/Research/Telecom/Text/Gen_info.doc'
   f11=open('C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/Coefficients.doc', 'wb')
   f12=open('C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/Coefficients_3.doc', 'wb')
   #fb12=open('C:/Users/ninar/OneDrive/Documents/Research/Telecom/Text/words.doc', 'wb')
   #fb13=open('C:/Users/ninar/OneDrive/Documents/Research/Telecom/Text/adjective.doc', 'wb')
   #fb14=open('C:/Users/ninar/OneDrive/Documents/Research/Telecom/Text/verb.doc', 'wb')
   #fb15=open('C:/Users/ninar/OneDrive/Documents/Research/Telecom/Text/adverb.doc', 'wb')
   #fb11=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase30_all.doc', 'wb')
   #fb12=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase30_noun.doc', 'wb')
   #fb13=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase30_adjective.doc', 'wb')
   #fb14=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase30_verb.doc', 'wb')
   #fb15=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase30_adverb.doc', 'wb')
   #fb11=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase40_all.doc', 'wb')
   #fb12=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase40_noun.doc', 'wb')
   #fb13=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase40_adjective.doc', 'wb')
   #fb14=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase40_verb.doc', 'wb')
   #fb15=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase40_adverb.doc', 'wb')
   #fb11=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase50_all.doc', 'wb')
   #fb12=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase50_noun.doc', 'wb')
   #fb13=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase50_adjective.doc', 'wb')
   #fb14=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase50_verb.doc', 'wb')
   #fb15=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase50_adverb.doc', 'wb')
   #fb11=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase60_70_all.doc', 'wb')
   #fb12=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase60_70_noun.doc', 'wb')
   #fb13=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase60_70_adjective.doc', 'wb')
   #fb14=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase60_70_verb.doc', 'wb')
   #fb15=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/Phase60_70_adverb.doc', 'wb')
   #fb11=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/All_all.doc', 'wb')
   #fb12=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/All_noun.doc', 'wb')
   #fb13=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/All_adjective.doc', 'wb')
   #fb14=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/All_verb.doc', 'wb')
   #fb15=open('C:/Users/Admin/Desktop/Vera/LSA_Vera/Workshops/ITIL/All_adverb.doc', 'wb')
  
   #f1=open(path_1,'wb')
   #analyser = SentimentIntensityAnalyzer()
   f11.write(bytes('Num, Lang, text,'+'Factor a  '+','+ '  Factor b  '+','+' Mistake of approximation  '+'\n', 'UTF-8'))
   f12.write(bytes('Num,' +'xx'+','+ '  yy '+'\n', 'UTF-8'))
   #fb12.write (bytes( 'Lang, noun, adjective, verbs, adverbs','UTF-8'))
   for i in a[0:9084]:  
      filename=path+'/'+str(i)
      filename1=str(i)
      print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
                     da={}
                     ds={}
                     dv={}
                     dd={}
                     dp={}
                     dad={}
                     d={}
                     s=" "
                     f11.write(bytes(str(i)+', ', 'UTF-8'))
                     f12.write(bytes(str(i)+', ', 'UTF-8'))
                     for line in file_object:
                                   line = line.rstrip('\n')
                                   k=k+1
                                   if len(line)>0:
                                      s=s+" "+line                                   
                     
                     #print(s)
                     s = re.sub('[^.,a-zA-Z0-9 \n\.]', '', s)
                     text_s=s
                     #print (s)
                     q=nltk.word_tokenize(s)
                     #print(q)
                     word_stem=[stemmer.stem(w).lower() for w in q if len(w) >0 and w.isalpha()]
                  
                     stopWordsE = set(stopwords.words('english'))
                     stopWordsE=[stemmer.stem(w).lower() for w in stopWordsE if len(w) >0 and w.isalpha()]
                     stopwords_e = [w for w in word_stem if w in stopWordsE]
                     #print(stopwords_e)
                     l=len(q)
                     if len(q)==0:
                        l=1
                     n_eng=len(stopwords_e) / l * 100
                     #print(n_eng)
                     stopWordsG = set(stopwords.words('german'))
                     stopwords_g = [w for w in word_stem if w in stopWordsG]
                     #print(stopwords_g)
                     n_ger=len(stopwords_g) / l * 100
                     #print(n_ger)
                     if n_ger>n_eng:
                        kkk="German"
                     else:
                        kkk="English"
                     #print (kkk)
                     #v=word_stem
                     v=([x  for x in word_stem if x and (x not in stopWordsE)])
                     print(v)
                     
                     my_dictionary=dict([])
                     z=[]
                     for w in v:
                        if w in my_dictionary:
                           my_dictionary[w]+=1
                        else:
                           my_dictionary[w]=1                           
                     max_count=len(my_dictionary)
                     min_count=1
                     print(my_dictionary)
                      
                     my_dictionary_z=dict([])         
                     for key,val in my_dictionary.items():
                        if val in my_dictionary_z:
                           my_dictionary_z[val]+=1
                        else:
                           my_dictionary_z[val]=1
                        z.append(val)
                     
                     
                     z.sort(reverse=False)
                     z.sort(reverse=True)
                     print(z)
                     print(my_dictionary_z)
                     
                     for b in my_dictionary_z:
                        print(my_dictionary_z[b])
                     xx=[]
                     yy=[]
                     
                     
                     
                     for b, b1 in my_dictionary_z.items():
                     #for b, b1 in items1[b,b1]:
                        xx.append(b)
                        yy.append(b1)
                     #xx.sort(reverse=True)
                     #yy.sort(reverse=True)
                     print(xx)
                     print(yy)
                     

                     #print(len(z))
                     
                     e=z[0:len(z)-1]
                     #print(len(z))
                     
                     #e=z[min_count:len(z)]
                     ee=[my_dictionary_z[val] for val in z][1:(len(z))]
                     ee=np.arange(len(my_dictionary))[1:(len(z))]
                     #print(ee)
                     #print(e)
                     
                     #print(len(v))
                     if len(v)>=0:
                        ttt=len(v)
                        if ttt==0:
                           ttt=1
                           
                        zz=round((float(len(my_dictionary))*100)/(float(ttt)),0)
                        #tt=('In total of words (Text-1) --%i. New words --%i. Percen new words-- %i'%( len(v),len( my_dictionary),int(zz)))
                        #print(tt)
                        xData1 = ee
                        yData1 = e
                        #print(xData1)
                        #print(yData1)
                        
                        z=[1/w for w in ee if w>0]
                        #print("z=",z)
                        z1=[(1/w)**2 for w in  ee if w>0]
                        #print("z1=",z1)
                        t=[ round(e[i]/ee[i],4)  for i in range(0,len(ee)) ]
                        aa=sum(e)*sum(z1)-sum(z)*sum(t)
                        
                        aaa=len(ee)*sum(z1)-sum(z)**2
                        bb=len(ee)*sum(t)-sum(z)*sum(e)
                        bbb=len(ee)*sum(z1)-sum(z)**2
                        if aa!=0 and aaa!=0 and bb!=0 and bbb!=0:
                            a=round((sum(e)*sum(z1)-sum(z)*sum(t))/(len(ee)*sum(z1)-sum(z)**2),3)
                            b=round((len(ee)*sum(t)-sum(z)*sum(e))/(len(ee)*sum(z1)-sum(z)**2),3)
                            y1=[round(a+b/w ,4) for w in ee]
                            s=[round((y1[i]-e[i])**2,4) for i in range(0,len(ee))]
                            sko=round(round((sum(s)/(len(ee)-1))**0.5,4)/(sum(y1)/len(ee)),4)
                            y1Data1=y1
                        else:
                            a=1.0
                            b=0.0
                            f11.write(bytes("\n", 'UTF-8'))
                            f12.write(bytes("\n", 'UTF-8'))
                        #print(filename1)
                        print("a=", a)
                        
                        print("b=", b)
                        print("sko=", sko)
                        
                        if a!="Nan":
                           f11.write(bytes(str(kkk)+','+str(text_s[:9])+','+str(a)+','+str(b)+','+str(sko)+"\n", 'UTF-8'))
                           
                           #plt.title('Zipf’s Rank-Frequency Distribution', size=14)
                           #plt.xlabel('Rank of word', size=14)
                           #plt.ylabel('Frequency of words', size=14)
                
                           #plt.plot(xData1, yData1, color='r', linestyle=' ', marker='o', label='Test')
                           #plt.plot(xData1, y1Data1, color='r',linewidth=2)
                     
                           #plt.legend(loc='best')
                           #plt.grid(True)
                           #plt.show()
                        #______________________________________________________________________________

                          
                        
                           f12.write(bytes(str(xx)+','+str(yy)+"\n", 'UTF-8'))
                           #plt.title('Zipf’s Quantity-Frequency Distribution', size=14)
                           #plt.xlabel('Frequency of the use the words', size=14)
                           #plt.ylabel('Number of words ', size=14)
                           
                           #plt.bar(xx, yy, color='b')
                           
                           #plt.plot(xData1, y1Data1, color='r',linewidth=2)
                     
                           
                           #plt.show()
                           
  
   f11.close()
   f12.close()
    
stopwords1=['the', 'a', 'in ', 'for', 'to', 'of', 'and', 'ABC', 'of', 'on', 'at',
          'or', 'if', 'end', 'were','each', 'was', 'as','has', 'how', 'it', 
           'may', 'often', 'be',  'done', 'these', 'all', 'etc', 'made',
           'make', ' the', 'about', 'also', 'always', 'as', 'can',
           'but', 'do', 'get', 'go', 'how', 'is', 'it',  'just', 'lot',
           'off', 'them', 'they', 'this', 'thus',  'up', 'us', 'say', 'very',
           'why', 'your', 'need', ' must', 'now', 'so', 'some',
           'became', 'still', 'stay', 'take', 'took', 'want', 'busy',
           'while', 'who', 'you', 'thank', 'new', 'psi',
           'get', 'our', 'out', 'set', 'such', 'take', 'have', 
           'than', 'their', 'then', 'well', 'in', 'when', 'his', 'even',
           'what', 'due', 'via', 'from', 'do', 'does', 'thus',
           'with', 'which', 'within', 'where', 'come', 'more',
           'there', 'their', 'be', 'between', 'been',  'through',
           'can', 'is', 'this', 'we', 'will', 'give', 'without', 'by',
           'about', 'does', 'not', 'that', 'no', 'but', 'are']

word_count(stopwords)
