import pandas as pd
import pickle as pk
from scipy import sparse as sp
from array import array
import numpy as np

import re


def fun(s):
    return re.sub(r'([\d]+)', '', s).lower()


p_df = pd.read_csv('/Users/richard/Desktop/660D Web Analytics/Final_project/The_Venetian Resort-Hotel-Casino.csv')
doc_complete = p_df['Overall_review']
list1 = []
for eachline in doc_complete:
    #     print(eachline)
    list1.append(eachline)
#          lines = filter(eachline.isalpha(), eachline)
# list = [doc_complete

newlist111 = []
for i in list1:
    i = i.split(" ")
    #     i = i.split()
    #     print(i)
    i = [item for item in (filter(lambda x: x.isalpha(), i))]
    # newlist111.append(list111(filter(lambda x : x.isalpha(), i)))
    newlist111.append(i)

#     for j in list1:
#         print(j)
print(newlist111)
# newlist

def magic(dumy):
    new_dumy = []
    super_dumy = []
    for i in dumy:
        new_dumy.append(';'.join(i))
    super_dumy = ';'.join(new_dumy).split(';')
    return super_dumy

list_new=magic(newlist111)

arr=np.array(list_new)

while '' in list_new:
    list_new.remove('')

data=pd.DataFrame(list_new)

data[data.isnull().values==True]

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = ''.join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join([ch for ch in stop_free if ch not in exclude])
    normalized = ''.join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
doc_clean = [clean(doc).split() for doc in list_new]

data=pd.DataFrame(doc_clean)

data2=data[data.isnull().values==False]

doc_clean=np.array(data2)