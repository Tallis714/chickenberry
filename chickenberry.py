#JPop Band Name and Hits Generator
#aka. chickenberry
#Jonisha McKiddy | Julie Evans


###import/corpus###
import re
import nltk
from nltk.corpus import knbc
jc=knbc.words()
c=nltk.corpus.words.words()
from nltk.corpus import PlaintextCorpusReader
#portal=r"C:\Users\JuJuBee Marie\Google Drive\linguistics\comp ling\chickenberry"
corpus_root=r"C:\\Users\ses71_000\Desktop\programming"
pc=PlaintextCorpusReader(corpus_root, 'portal 12text.txt')
#cfd_pc=nltk.ConditionalFreqDist(nltk.bigrams(pc))
#cpd_pc=nltk.ConditionalProbDist(cfd_pc, nltk.MLEProbDist)

###dictionary###
f=open('C:\\Users\ses71_000\Desktop\edict.csv', encoding='utf-8')
#def searchable(w):
    #[word for line in f for word in line.split()]
    #print(w, word)
    
#srch=[word for word in f for word in line.split()]


read=f.readlines()
char={}
for line in read:
    l=line
    str.replace(l,',,,,,,,,,,,,,,,,,,,,','')
    p=re.split('\||\|',l)
    key=p[1]
    value=p[0]
    char[key]=value
#still only adds the last line to dict
    #if key in mydict:
        #print(value)
    #else: print('Not in Dictionary')
        #mydict={}
        #str.replace(l,'||',',')
        #str.replace(l,'|',',')
        #str.replace(l,')','),')
        #str.split(',')
        #return l
        #noundict=[xxx if (n) in f]
        #for word in line:
            #key=[0]
            #value=[3]
            #mydict= dict({key:value})
    #dict(one=1, two=2, three=3)
    #{'one': 1, 'two': 2, 'three': 3}
    #dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    #dict([('two', 2), ('one', 1), ('three', 3)])
    #dict({'three': 3, 'one': 1, 'two': 2})
f.close()

#def revlook(d,v):
    #for key in mydict:
        #if d[key] == v:
            #return key
        #else: print("Error")

###intro/survey###
print("This is a JPop Band Name Generater.\n")
###while loop or not? to repeat whole program... "Do you wish to try again? (start over)"
answer=input("Will you answer a short survey to find out what your JPop Band Name would be?\n(type YES or NO to continue)\n")
if answer == "YES":
    print("Okay! Here goes... \n(use ONLY single word answers)\n")
    quest1=input("What is your favourite food?\n")
    quest2=input("What is your favourite word?\n")
    quest3=input("What is your favourite animal?\n")
    quest4=input("What kind of weather do you like?\n")
    quest5=input("What is a thing that you like the most?\n")
    quest6=input("What is your mood right now?\n")
    ###search###
    #for w in jc
        #word1=[w for w if re.search(noundict, jc)]
        #take input word
        #>>> generate word from c
        #search noundict for equivalent
        #generate word from jc <<< do we even need this step?
        #return that word
    #word1=value for key if quest1 in mydict
    def word1():
        for key in char:
            if quest1 is key:
                print(value)
            else: print('Not in Dictionary')
    def word2():
        for key in char:
            if quest6 is key:
                print(value)
            else: print('Not in Dictionary')
    def word3():
        for key in char:
            if quest4 is key:
                print(value)
            else: print('Not in Dictionary')
    ###product###
    bname1= word1()#cpd_pc[quest3].generate()
    bname2='lol'#cpd_pc[quest1].generate()
    hname1='lol'#cpd_pc[quest2].generate()
    hname2='lol'#cpd_pc[quest6].generate()
    hname3='lol'#cpd_pc[quest4].generate()

    print()
    print("CONGRATS!")
    print("Your band name is...\n" "'+word1+bname2'")
    print("Your top hit songs are: \n 1.'"+hname1+"'\n 2.'"+hname2+"'\n 3.'"+hname3+"'\n")
    print("Thanks for joining us.")
elif answer == "NO":
    print("Sorry to see you go so soon.")
else: print("Not an answer choice.")

#search
#for w in c:
    #word1=[w.similar if re.search(quest1, c)]
    #word2=[w.similar if re.search(quest2, c)]
    #word3=[w.similar if re.search(quest3, c)]
    #word4=[w.similar if re.search(quest4, c)]
    #word5=[w.similar if re.search(quest5, c)]
    #word6=[w.similar if re.search(quest6, c)]
    #word7=[w.similar if re.search(quest7, c)]
    
    ###or something like this
    ###see if can search for capital and lower case

#generate
    #decide how to create/generate name
    #decide whether name is english or japanese (and whether in kanji or not if jap)
    #decide how to defferenciate boyband and girlband or not
    #decide if name is in all caps or not
    #generate song name(s) seperately

###compling.hss.ntu.edu.sg/ntumc (source info)
