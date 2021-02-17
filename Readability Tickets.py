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

from settings import stem
from nltk.corpus import stopwords
from nltk.stem import  SnowballStemmer

stemmer = SnowballStemmer(stem)
#_____________________________________________________________________________________________________________________________
# META-KNOWLEDGE EXTRACTION:

# MAIN STAGES:
# STAGE 1. Tickets Corpus Reading, Preprocessing and English language filtering
# STAGE 2. Tickets Descriptioin Length calculating (number of words)
# STAGE 3. Calculating the (i) number of PoS and (ii) unique PoS distribution
# STAGE 4. Identifying basic Zipf's law coefficients 
# STAGE 5. Writing of Text length, number of PoS, unique PoS distribution and Zipf's law coefficients in the *.csv file
#_______________________________________________________________________________________________________________________________
def word_count(stopword):
   k=0
   
   a=sorted(os.listdir(path))
   
   f11=open('C:/Users/all1.doc', 'wb')
   fb12=open('C:/Users/words1.doc', 'wb')

   f11.write(bytes('Num, Lang, % eng, % ger, text, All words ,Unique words, % of Unique words, noun , Unique noun , % of Unique NN (noun), adjective, Unique adjective, % of Unique JJ + JJR  (adjective), verb, Unique verb, % of Unique VB (verb), adverb, Unique adverb, % of Unique RB (adverb)'+'\n', 'UTF-8'))
   fb12.write (bytes( 'Lang, noun, adjective, verbs, adverbs','UTF-8'))
   
#______________________STAGE 1. Tickets Corpus Reading, Preprocessing and English language filtering____________________________
  
   for i in a[0:N]:  
      filename=path+'/'+str(i)
      filename1=str(i)
      
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
                     for line in file_object:
                                   line = line.rstrip('\n')
                                   k=k+1
                                   if len(line)>0:
                                      s=s+" "+line                                   
                    
                     s = re.sub('[^.,a-zA-Z0-9 \n\.]', '', s)
                     text_s=s
                     
                     q=nltk.word_tokenize(s)
                     word_stem=[stemmer.stem(w).lower() for w in q if len(w) >0 and w.isalpha()]
                  
                     stopWordsE = set(stopwords.words('english'))

                     stopwords_e = [w for w in word_stem if w in stopWordsE]
                     l=len(q)
                     if len(q)==0:
                        l=1
                     n_eng=len(stopwords_e) / l * 100
                     
                     stopWordsG = set(stopwords.words('german'))
                     stopwords_g = [w for w in word_stem if w in stopWordsG]
                     n_ger=len(stopwords_g) / l * 100
                     
                     if n_ger>n_eng:
                        kkk="German"
                     else:
                        kkk="English"
                     print (kkk)
                     

#_______________________________________ STAGE 2. Text length calculating______________________________________                          
                     m1=m.split(' ')
                     m=list(m1)

                     text=(" ").join(m)
                    
                     ma0=""
                     for w in m:
                        if w in d:
                           d[w]+=1
                           ma0 += str(w)
                           ma0 +=', '
                           
                        else:
                           d[w]=1
                           ma0 += str(w)
                           ma0 +=', '
                     z=[]
                     ma00=ma0.split(' ')
                     
                     fb12.write(bytes('\n', 'UTF-8'))
                     
                     
                     f11.write(bytes(str(kkk)+', '+str(n_eng)+','+str(n_ger)+','+str(text_s[:9])+',', 'UTF-8'))
                     
                     fb12.write(bytes(str(filename1)+', '+str(kkk)+',', 'UTF-8'))
                     
                     for key,val in d.items():
                        z.append(val)      
                     
                     z.sort(reverse=True)
                     mm=len(m)
                     f11.write(bytes(str(mm)+', ', 'UTF-8'))
                    
                     e=z[0:mm]
                     
                     k = len(e)-1
                     while k >=1:
                        ppp=k*e[k]
                        
                        k -= 1
              
                     pairs = list(d.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     z=round((float(len(d))*100)/(float(len(m))),0)
                     if len(m)>100:
                        ff=100
                     else:
                        ff=len(m)
                     
                     f11.write(bytes(str(len(d))+', '+str(z)+',', 'UTF-8'))   
                     
                     m=""
                     for i in a:
                        s=i[0]
                        s1=str(i[1])
                        
                        if s1==wr or s1==wr1 or s1==wr2:
                           m=m+s+' '
                     m2=m.split(' ')
                  
                     ma=list(m2)
                     if ma==['']:
                        ma=[]
                     if ma!=['']:
                        ma=ma[:-1]
                     ma1=""
                     ma11=[]
                     for w in ma:
                        if w in da:
                           ma1 += str(w)
                           ma11.append(str(w))
                           ma1 +='. '
                           da[w]+=1
                        else:
                           da[w]=1
                           ma1 += str(w)
                           ma11.append(str(w))
                           ma1 +='. '
                     print('ma11=',ma11)
                     
# ________________________STAGE 3. Calculating the number of PoS and unique PoS distribution_______________________

                     c=['NN', 'NNP', 'NNS', 'JJ', 'JJR', 'VB','VBZ', 'VBG','VBN', 'RB']
                                         
                     a=nltk.pos_tag(q)
                     
                     m=""
                     for i in a:
                        s=i[0]
                        s1=str(i[1])
                        wr=str(c[0])
                        wr1=str(c[1])
                        wr2=str(c[2])
                        wr3=str(c[3])
                        wr4=str(c[4])
                        wr5=str(c[5])
                        wr6=str(c[6])
                        wr7=str(c[7])
                        wr8=str(c[8])
                        wr9=str(c[9])
                        m=m+s+' '
                         
                     #____________nouns_______________________________
                     

                     ma11=ma1.split(' ')
                     
                     fb12.write(bytes(str(ma1)+',', 'UTF-8'))
                     
                     za=[]
                     for key,val in da.items():
                        za.append(val)
                     
                     za.sort(reverse=True)
                     mma=len(ma)
                     
                     e=za[0:mma]
                     pairs = list(da.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     if ma==[]:
                        za=0
                     if ma!=[]:
                        za=round((float(len(da))*100)/(float(len(ma))),0)
                     f11.write(bytes(str(len(ma))+', '+str(len(da))+', '+str(za)+', ', 'UTF-8'))
                     
                     ee=np.arange(len(da))
                          
                     m=""
                     for i in a:
                        s=i[0]
                        s1=str(i[1])
                        
                        if s1==wr3 or s1==wr4:
                           m=m+s+' '
                     
                     
                     m3=m.split(' ')
                     
                     ms=list(m3)
                     if ms==['']:
                        ms=[]
                     if ms!=['']:
                        ms=ms[:-1]
                     
                     ma2=""
                     ma22=[]
                     for w in ms:
                        if w in ds:
                           ds[w]+=1
                           ma2 += str(w)
                           ma22.append(str(w))
                           ma2 +='. '
                        else:
                           ds[w]=1
                           ma2 += str(w)
                           ma22.append(str(w))
                           ma2 +='. '
                     #________________adjectives______________________________
   
                     zs=[]
                     
                     ma22=ma2.split(' ')
                     
                     fb12.write(bytes( str(ma2)+',', 'UTF-8'))
                     
                     for key,val in ds.items():
                        zs.append(val)      
                     
                     zs.sort(reverse=True)
                     mms=len(ms)
                     
                     e=zs[0:mms]     
                     pairs = list(ds.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     if ms==[]:
                        zs=0
                     if ms!=[]:
                        zs=round((float(len(ds))*100)/(float(len(ms))),0)
                     f11.write(bytes(str(len(ms))+', '+str(len(ds))+', '+str(zs)+', ', 'UTF-8'))

                     
                     print('adjective:'+str(len(ms)),'; Unique adjective:'+str(len(ds)),'; % of Unique JJ + JJR(adjective):'+str(zs))
                     
                     ee=np.arange(len(ds))
                     
                     m=""
                     for i in a:
                        s=i[0]
                        s1=str(i[1])
                        if s1==wr5 or s1==wr6 or s1==wr7 or s1==wr8:
                           m=m+s+' '
                     m4=m.split(' ')
                     
                     mv=list(m4)
                     if mv==['']:
                        mv=[]
                     if mv!=['']:
                        mv=mv[:-1]
                     
                     ma3=""
                     ma33=[]
                     for w in mv:
                        if w in dv:
                           dv[w]+=1
                           ma3 += str(w)
                           ma33.append(str(w))
                           ma3 +='. '
                        else:
                           dv[w]=1
                           ma3 += str(w)
                           ma33.append(str(w))
                           ma3 +='. '
                     #_____________verbs_________________________________________
                           
                     zv=[]
                     
                     ma33=ma3.split(' ')
                     
                     
                     fb12.write(bytes(str(ma3)+',', 'UTF-8'))
                     
                     for key,val in dv.items():
                        zv.append(val)
                     
                     zv.sort(reverse=True)
                     mmv=len(mv)
                     
                     e=zv[0:mmv]
                         
                     pairs = list(dv.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     if mv==[]:
                        zv=0
                     if mv!=[]:
                        zv=round((float(len(dv))*100)/(float(len(mv))),0)
                     
                     f11.write(bytes(str(len(mv))+', '+str(len(dv))+', '+str(zv)+', ', 'UTF-8'))

                      
                     print('verb:'+str(len(mv)),'; Unique verb:'+str(len(dv)),'; % of Unique VB (verb):'+str(zv))
                     
                     ee=np.arange(len(dv))
                     
                     m=""
                     for i in a:
                        s=i[0]
                        s1=str(i[1])
                        if s1==wr9:
                           m=m+s+' '
                     m7=m.split(' ')
                     mad=list(m7)
                     if mad==['']:
                        mad=[]
                     if mad!=['']:
                        mad=mad[:-1]
                     ma7=""
                     ma77=[]
                     for w in mad:
                        if w in dad:
                           dad[w]+=1
                           ma7 += str(w)
                           ma77.append(str(w))
                           ma7 +='. '
                        else:
                           dad[w]=1
                           ma7 += str(w)
                           ma77.append(str(w))
                           ma7 +='. '
                     #__________adverbs_______________________________
                     
                     zad=[]
                    
                     ma77=ma7.split(' ')
                     
                     fb12.write(bytes(str(ma7), 'UTF-8'))
                     fb12.write(bytes('\n', 'UTF-8'))
                     for key,val in dad.items():
                        zad.append(val)
                     
                     zad.sort(reverse=True)
                     mmad=len(mad)
                     
                     e=zad[0:mmad]
                         
                     pairs = list(dad.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     if mad==[]:
                        zv=0
                     if mad!=[]:
                        zv=round((float(len(dad))*100)/(float(len(mad))),0)
                     f11.write(bytes(str(len(mad))+', '+str(len(dad))+', '+str(zv)+'\n', 'UTF-8'))

                     
                     fb.write(bytes(str(kkk)+','+str(yy[0])+','+str(yy[1])+','+str(yy[2])+','+str(yy[3]), 'UTF-8'))
                     fb.write(bytes('\n', 'UTF-8'))    
                    
                     ee=np.arange(len(dad))
                   
   f11.close()
   fb12.close()

#____________________ STAGE 4. Identifying basic Zipf's law coefficients _________________________________________   

   f11=open('C:/Users/Coefficients.doc', 'wb')
   f12=open('C:/Users/Coefficients_3.doc', 'wb')

   f11.write(bytes('Num, Lang, text,'+'Factor a  '+','+ '  Factor b  '+','+' Mistake of approximation  '+'\n', 'UTF-8'))
   f12.write(bytes('Num,' +'xx'+','+ '  yy '+'\n', 'UTF-8'))

   for i in a[0:N]:  
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
                     
                     
                     s = re.sub('[^.,a-zA-Z0-9 \n\.]', '', s)
                     text_s=s
                     
                     q=nltk.word_tokenize(s)
                     
                     word_stem=[stemmer.stem(w).lower() for w in q if len(w) >0 and w.isalpha()]
                  
                     stopWordsE = set(stopwords.words('english'))
                     stopWordsE=[stemmer.stem(w).lower() for w in stopWordsE if len(w) >0 and w.isalpha()]
                     stopwords_e = [w for w in word_stem if w in stopWordsE]
                     
                     l=len(q)
                     if len(q)==0:
                        l=1
                     n_eng=len(stopwords_e) / l * 100
                     
                     stopWordsG = set(stopwords.words('german'))
                     stopwords_g = [w for w in word_stem if w in stopWordsG]
                     
                     n_ger=len(stopwords_g) / l * 100
                     
                     if n_ger>n_eng:
                        kkk="German"
                     else:
                        kkk="English"
                     
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
                    
                        xx.append(b)
                        yy.append(b1)
                    
                     print(xx)
                     print(yy)
                     
                     e=z[0:len(z)-1]
          ee=[my_dictionary_z[val] for val in z][1:(len(z))]
                     ee=np.arange(len(my_dictionary))[1:(len(z))]
                     
                     if len(v)>=0:
                        ttt=len(v)
                        if ttt==0:
                           ttt=1
                           
                        zz=round((float(len(my_dictionary))*100)/(float(ttt)),0)
                      
                        xData1 = ee
                        yData1 = e
                      
                        z=[1/w for w in ee if w>0]
                       
                        z1=[(1/w)**2 for w in  ee if w>0]
                        
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
                        
                        print("a=", a)
                        
                        print("b=", b)
                        print("sko=", sko)
                        
                        if a!="Nan":
                           f11.write(bytes(str(kkk)+','+str(text_s[:9])+','+str(a)+','+str(b)+','+str(sko)+"\n", 'UTF-8'))
                           
                        f12.write(bytes(str(xx)+','+str(yy)+"\n", 'UTF-8'))
                          
                           
  
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
