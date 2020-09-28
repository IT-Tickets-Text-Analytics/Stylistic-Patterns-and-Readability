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

def word_count(stopword):
   #path='C:/Users/ninar/OneDrive/Documents/Research/Telecom/Tickets_separated'
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/1_Research_Second_Iteration/ITIL_noun'
   
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Bo=s1
   
  #________________________________________________________
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/1_Research_Second_Iteration/ITIL_adj'
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Re=s1
   #___________________________________________________________
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/1_Research_Second_Iteration/ITIL_verb'
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Sc=s1
   #_________________________________________________________ 
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/1_Research_Second_Iteration/ITIL_avd'
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+str(i)
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   Fa=s1
   #_________________________________________________________ 
   k_b=0
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/'
   k=0
   fb=open('C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/ITIL.doc', 'wb')
   a=sorted(os.listdir(path))
   #k_w=0
   #k_o=0
   fb.write(bytes('num, length, lang, noun, adjective, verb, adverb'+'\n', 'UTF-8'))
   Bo_stem=[stemmer.stem(w).lower() for w in Bo if len(w) >1 and w.isalpha()]
   
   Re_stem=[stemmer.stem(w).lower() for w in Re if len(w) >1 and w.isalpha()]
   
   Sc_stem=[stemmer.stem(w).lower() for w in Sc if len(w) >1 and w.isalpha()]
   Fa_stem=[stemmer.stem(w).lower() for w in Fa if len(w) >1 and w.isalpha()]
   print(Fa_stem)
   
   path='C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/Texts'
   k=0
   #fb=open('Text.txt', 'wb')
   
   a=sorted(os.listdir(path))
   #path_1='C:/Users/ninar/OneDrive/Documents/Research/Telecom/Text/Gen_info.doc'
   f11=open('C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/all.doc', 'wb')
   fb12=open('C:/Users/ninar/OneDrive/Documents/RESEARCH/Telekom/2_Research_Tasks/POS.doc', 'wb')
   
  
   #f1=open(path_1,'wb')
   f11.write(bytes('Num, Lang, % eng, % ger, text, All words ,Unique words, % of Unique words, noun , Unique noun , % of Unique NN (noun), adjective, Unique adjective, % of Unique JJ + JJR  (adjective), verb, Unique verb, % of Unique VB (verb), adverb, Unique adverb, % of Unique RB (adverb)'+'\n', 'UTF-8'))
   fb12.write (bytes( 'Lang, noun, adjective, verbs, adverbs','UTF-8'))
   #for i in a[0:2]:
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
                     #print(str(i))
                     f11.write(bytes(str(i)+', ', 'UTF-8'))
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
                     word_stem=[stemmer.stem(w).lower() for w in q if len(w) >0 and w.isalpha()]
                     #print(word_stem)
                     stopWordsE = set(stopwords.words('english'))
                     stopWordsE=[stemmer.stem(w).lower() for w in stopWordsE if len(w) >0 and w.isalpha()]
                     #print(stopWordsE)
                     
                     stopwords_e = [w for w in word_stem if w in stopWordsE]
                     l=len(q)
                     if len(q)==0:
                        l=1
                     n_eng=len(stopwords_e) / l * 100
                     #print(n_eng)
                     stopWordsG = set(stopwords.words('german'))
                     stopwords_g = [w for w in word_stem if w in stopWordsG]
                     n_ger=len(stopwords_g) / l * 100
                     #print(n_ger)
                     if n_ger>n_eng:
                        kkk="German"
                     else:
                        kkk="English"
                     print (kkk)
                     
                     #print(len(q))
                     
                     #print(nltk.pos_tag(q))
                     
                     c=['NN', 'NNP', 'NNS', 'JJ', 'JJR', 'VB','VBZ', 'VBG','VBN', 'RB']
                     #print(c[0])
                     #n=[stemmer.stem(w).lower() for w in q if len(w)>1 and w.isalpha()]
                     #print(n)
                     
                     #words=[ w for w in n if w not in stopword]
                     
                     a=nltk.pos_tag(q)
                     
                     #oo=length(a)
                     #print(a)
                     
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
                           
                     m1=m.split(' ')
                     m=list(m1)

                     text=(" ").join(m)
                     #fb11.write(bytes(text+'\n', 'UTF-8'))
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
                     
                     #f11.write(bytes('_________________________________________' +'\n', 'UTF-8'))
                     f11.write(bytes(str(kkk)+', '+str(n_eng)+','+str(n_ger)+','+str(text_s[:9])+',', 'UTF-8'))
                     #fb12.write(bytes('_________________________________________' +'\n', 'UTF-8'))
                     fb12.write(bytes(str(filename1)+', '+str(kkk)+',', 'UTF-8'))
                     #f11.write(bytes('All words: ', 'UTF-8'))
                     #fb11.write(bytes(str(ma0), 'UTF-8'))
                     #fb11.write(bytes('\n', 'UTF-8'))
                     for key,val in d.items():
                        z.append(val)      
                     #print('k=',k)
                     z.sort(reverse=True)
                     mm=len(m)
                     f11.write(bytes(str(mm)+', ', 'UTF-8'))
                                          
                     #print('mm=',mm)
                     e=z[0:mm]
                     
                     k = len(e)-1
                     while k >=1:
                        ppp=k*e[k]
                        #print(ppp,'  ', k, ', ', e[k])
                        k -= 1
              
                     pairs = list(d.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     z=round((float(len(d))*100)/(float(len(m))),0)
                     if len(m)>100:
                        ff=100
                     else:
                        ff=len(m)
                     #f11.write(bytes('Unique words: '+str(len(d))+', % of Unique words:'+str(z), 'UTF-8'))
                     f11.write(bytes(str(len(d))+', '+str(z)+',', 'UTF-8'))   
                     #f11.write(bytes('\n', 'UTF-8'))
                     
                     #print('')
                     #print('# doc:'+str(i))
                     #print('Words:'+str(len(m)),'; Unique words:'+str(len(d)),'; % of Unique words:'+str(z))
                     #print(pairs[0:ff])
                     
                     #ee=np.arange(len(d))
                     #plt.title('Distribution of frequencies of use of all words in the text', size=14)
                     #plt.xlabel('Serial number of new words', size=14)
                     #plt.ylabel('Frequency of the use of new words', size=14)
                     #plt.plot(ee,e, color='r', linestyle=' ', marker='o', label='Test')
                     #plt.legend(loc='best')
                     #plt.show()
                     m=""
                     for i in a:
                        s=i[0]
                        s1=str(i[1])
                        
                        if s1==wr or s1==wr1 or s1==wr2:
                           m=m+s+' '
                     m2=m.split(' ')
                     #print("m2=",m2)
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
                     #print('ma11=',ma11)
                     ma11=[stemmer.stem(w).lower() for w in ma11 if len(w) >0 and w.isalpha()]
                     ma11=[ w for w in ma11 if w not in stopWordsE]
                     print('ma11=',ma11)
                     
                     #____________nouns_______________________________
                     b=[]
                  
                     yy=[]
                     #print('_______________________________________________________')
                     try:
                        #print("lll")
                        b.append(sum([B[Bo_stem.index(w)] for w in ma11  if w in Bo_stem]))
                        print("b_nouns=",b)
                        yy.append(sum([ma11.count(w) for w in  Bo_stem]))
                        #print('Nouns=',  yy[0])
                     except:
                        pass 

                     #___________________________________________

                     ma11=ma1.split(' ')
                     #f1.write(bytes('_________________________________________' +'\n', 'UTF-8'))
                     #f1.write(bytes(str(filename) +'\n', 'UTF-8'))
                     #fb12.write(bytes('noun: ', 'UTF-8'))
                     fb12.write(bytes(str(ma1)+',', 'UTF-8'))
                     #fb12.write(bytes('\n', 'UTF-8'))
                     za=[]
                     for key,val in da.items():
                        za.append(val)
                     #print(za)
                     #f1.write(bytes(str(za)+'\n', 'UTF-8'))
                     za.sort(reverse=True)
                     mma=len(ma)
                     #print('mm=',mma)
                     e=za[0:mma]
                     pairs = list(da.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     if ma==[]:
                        za=0
                     if ma!=[]:
                        za=round((float(len(da))*100)/(float(len(ma))),0)
                     f11.write(bytes(str(len(ma))+', '+str(len(da))+', '+str(za)+', ', 'UTF-8'))
                     #f11.write(bytes('noun:'+str(len(ma))+', Unique noun:'+str(len(da))+', % of Unique NN (noun):'+str(za), 'UTF-8'))
                     #f11.write(bytes('\n', 'UTF-8'))
                     #print(pairs[0:len(ma)])
                     ee=np.arange(len(da))
                     #plt.title('Distribution of frequencies of use of NN (noun) in the text', size=14)
                     #plt.xlabel('Serial number of new words', size=14)
                     #plt.ylabel('Frequency of the use of new words', size=14)
                     #plt.plot(ee,e, color='r', linestyle=' ', marker='o', label='Test')
                     #plt.legend(loc='best')
                     #plt.show()
                                       
                     m=""
                     for i in a:
                        s=i[0]
                        s1=str(i[1])
                        
                        if s1==wr3 or s1==wr4:
                           m=m+s+' '
                     
                     #print("m=",m)
                     m3=m.split(' ')
                     #print("m3=",m3)
                     ms=list(m3)
                     if ms==['']:
                        ms=[]
                     if ms!=['']:
                        ms=ms[:-1]
                     #print("ms=",ms)
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
                     ma22=[stemmer.stem(w).lower() for w in ma22 if len(w) >0 and w.isalpha()]
                     ma22=[ w for w in ma22 if w not in stopWordsE]
                     print('ma22=',ma22)
                     #________________adjectives______________________________

                     try:
                        b.append(sum([R[Re_stem.index(w)] for w in ma22  if w in Re_stem]))
                        print("b_adjectives=",b)
                        yy.append(sum([ma22.count(w) for w in  Re_stem]))
                        #print('Adjectives=', yy[1])
                     except:
                        pass
                     #______________________________________________      
                     zs=[]
                     #print("ma2=","\n", ma2)
                     ma22=ma2.split(' ')
                     #fb12.write(bytes('adjective: ' , 'UTF-8'))
                     fb12.write(bytes( str(ma2)+',', 'UTF-8'))
                     #fb12.write(bytes('\n', 'UTF-8'))
                     for key,val in ds.items():
                        zs.append(val)      
                     #print(zs)
                     #f1.write(bytes(str(zs)+'\n', 'UTF-8'))
                     
                     zs.sort(reverse=True)
                     mms=len(ms)
                     #print('mm=',mms)
                     e=zs[0:mms]     
                     pairs = list(ds.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     if ms==[]:
                        zs=0
                     if ms!=[]:
                        zs=round((float(len(ds))*100)/(float(len(ms))),0)
                     f11.write(bytes(str(len(ms))+', '+str(len(ds))+', '+str(zs)+', ', 'UTF-8'))

                     #f11.write(bytes('adjective:'+str(len(ms))+', Unique adjective:'+str(len(ds))+', % of Unique JJ + JJR (adjective):'+str(zs), 'UTF-8'))
                     #f11.write(bytes('\n', 'UTF-8'))
     
                     print('adjective:'+str(len(ms)),'; Unique adjective:'+str(len(ds)),'; % of Unique JJ + JJR(adjective):'+str(zs))
                     #print(pairs[0:len(ms)])
                     ee=np.arange(len(ds))
                     #plt.title('Distribution of frequencies of use of JJ (adjective) in the text', size=14)
                     #plt.xlabel('Serial number of new words', size=14)
                     #plt.ylabel('Frequency of the use of new words', size=14)
                     #plt.plot(ee,e, color='r', linestyle=' ', marker='o', label='Test')
                     #plt.legend(loc='best')
                     #plt.show()

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
                     #print('mv=',mv)
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
                     ma33=[stemmer.stem(w).lower() for w in ma33 if len(w) >0 and w.isalpha()]
                     ma33=[ w for w in ma33 if w not in stopWordsE]
                     print('ma33=',ma33)
                     #_____________verbs_________________________________________
                     try:
                        print("Sc_stem=",Sc_stem)
                        yy.append(sum([ma33.count(w) for w in  Sc_stem]))
                        print(len(yy))
                        print("Sum=",sum([SS[Sc_stem.index(w)] for w in ma33 if w in Sc_stem]))
                        b.append(sum([SS[Sc_stem.index(w)] for w in ma33 if w in Sc_stem]))
                        print("b_verbs=",b)
                        
                        
                        if len(yy)==2:
                           yy.append('0.0')
                        print('Verbs=',  yy[2])
                     except:
                        pass  

                     #___________________________________________________________      
                     zv=[]
                     #print("ma3=",ma3)
                     ma33=ma3.split(' ')
                     
                     #fb12.write(bytes('verb: ', 'UTF-8'))
                     fb12.write(bytes(str(ma3)+',', 'UTF-8'))
                     #fb12.write(bytes('\n', 'UTF-8'))
                     for key,val in dv.items():
                        zv.append(val)
                     #print(zv)
                     #f1.write(bytes(str(zv)+'\n', 'UTF-8'))
                     zv.sort(reverse=True)
                     mmv=len(mv)
                     #print('mm=',mmv)
                     e=zv[0:mmv]
                         
                     pairs = list(dv.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     if mv==[]:
                        zv=0
                     if mv!=[]:
                        zv=round((float(len(dv))*100)/(float(len(mv))),0)
                     #f11.write(bytes('verb:'+str(len(mv))+', Unique verb:'+str(len(dv))+', % of Unique VB (verb):'+str(zv), 'UTF-8'))
                     f11.write(bytes(str(len(mv))+', '+str(len(dv))+', '+str(zv)+', ', 'UTF-8'))

                     #f11.write(bytes('\n', 'UTF-8'))  
                     print('verb:'+str(len(mv)),'; Unique verb:'+str(len(dv)),'; % of Unique VB (verb):'+str(zv))
                     #print(pairs[0:len(mv)])
                     ee=np.arange(len(dv))
                     #plt.title('Distribution of frequencies of use of VB (verb) in the text', size=14)
                     #plt.xlabel('Serial number of new words', size=14)
                     #plt.ylabel('Frequency of the use of new words', size=14)
                     #plt.plot(ee,e, color='r', linestyle=' ', marker='o', label='Test')
                     #plt.legend(loc='best')
                     #plt.show()
                     
                     #if askyesno('Verify', 'Do you want to continue?'):
                        #pass      
                     #else:
                        #exit()  

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
                     ma77=[stemmer.stem(w).lower() for w in ma77 if len(w) >0 and w.isalpha()]
                     ma77=[ w for w in ma77 if w not in stopWordsE]
                     print('ma77=',ma77)
                     ##_____________adverbs_________________________________________
                     
                     try:
                        b.append(sum([F[Fa_stem.index(w)] for w in ma77  if w in Fa_stem]))
                                               
                        print("Fa_stem=",Fa_stem)
                        print("b_adverbs=",b)
                        yy.append(sum([ma77.count(w) for w in  Fa_stem]))
                        print('Adverbs=', yy[3])
                        print(yy)
                     except:
                        pass      
                  
                                          

                     #_______________________________________
                     zad=[]
                     #print(ma7)
                     
                     ma77=ma7.split(' ')
                     #fb12.write(bytes('adverb:', 'UTF-8'))
                     fb12.write(bytes(str(ma7), 'UTF-8'))
                     fb12.write(bytes('\n', 'UTF-8'))
                     for key,val in dad.items():
                        zad.append(val)
                     #print(zad)
                     #f1.write(bytes(str(zad)+'\n', 'UTF-8'))
                     zad.sort(reverse=True)
                     mmad=len(mad)
                     #print('mm=',mmad)
                     e=zad[0:mmad]
                         
                     pairs = list(dad.items())
                     pairs.sort(key=lambda x: x[1], reverse=True)
                     if mad==[]:
                        zv=0
                     if mad!=[]:
                        zv=round((float(len(dad))*100)/(float(len(mad))),0)
                     f11.write(bytes(str(len(mad))+', '+str(len(dad))+', '+str(zv)+'\n', 'UTF-8'))
                     
                     print('Verbs=', yy[2])
                     print('Adjectives=', yy[1])
                     print('Nouns=', yy[0])
                     print('Adverbs=', yy[3])
                     fb.write(bytes(str(kkk)+','+str(yy[0])+','+str(yy[1])+','+str(yy[2])+','+str(yy[3]), 'UTF-8'))
                     fb.write(bytes('\n', 'UTF-8'))    
                     #f11.write(bytes('adverb:'+str(len(mad))+', Unique adverb:'+str(len(dad))+', % of Unique RB (adverb):'+str(zv), 'UTF-8'))
                     #f11.write(bytes('\n', 'UTF-8')) 
                    # print('adverb:'+str(len(mad)),'; Unique adverb:'+str(len(dad)),'; % of Unique RB (adverb):'+str(zad))
                     #print(pairs[0:len(mv)])
                     ee=np.arange(len(dad))
                     #plt.title('Distribution of frequencies of use of RB (adverb) in the text', size=14)
                     #plt.xlabel('Serial number of new words', size=14)
                     #plt.ylabel('Frequency of the use of new words', size=14)
                     #plt.plot(ee,e, color='r', linestyle=' ', marker='o', label='Test')
                     #plt.legend(loc='best')
                     #plt.show()
                     
                     
                     #result=messagebox.askyesno("Continue", "Do you want to continue?")
                     #if  result== True:
                        
                        #pass
                     #else:
                        #sys.exit()
                     
   #fb.close()
   f11.close()
   fb12.close()
   #fb13.close()
   #fb14.close()
   #fb15.close()
B=[1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0,
   1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,
   1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,
   1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0,1.0,1.0,1.0,1.0, 1.0,
   1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0,1.0,1.0,1.0, 1.0, 1.0]
R=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

SS=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

F=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
   1.0, 1.0, 1.0]

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
