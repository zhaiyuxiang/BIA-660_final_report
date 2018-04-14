"""
Reference: https://www.kaggle.com/adiljadoon/word-cloud-with-python/notebook
"""

import numpy as np # linear algebra
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
#matplotlib inline
import os.path

from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS


mpl.rcParams['figure.figsize']=(8.0,6.0)    #(6.0,4.0)
mpl.rcParams['font.size']=12                #10 
mpl.rcParams['savefig.dpi']=100             #72 
mpl.rcParams['figure.subplot.bottom']=.1 

stopwords = set(STOPWORDS)
stopwords.add("hotel")
stopwords.add("hotels")
stopwords.add("Basically")
stopwords.add("every")
stopwords.add("Nan")
stopwords.add("thing")
stopwords.add("us")
stopwords.add("think")
stopwords.add("made")


# Add extra stop words if provided
#if extra_stopwords is not None:
#    [stopwords.add(word) for word in extra_stopwords]

data_Venetian_pos = pd.read_csv("C:/Users/Nitin/Desktop/data_gathering/The_Venetian_pos_review.csv")
data_Caesars_pos = pd.read_csv("C:/Users/Nitin/Desktop/data_gathering/The_Venetian_pos_review.csv")
data_Wynn_pos = pd.read_csv("C:/Users/Nitin/Desktop/data_gathering/wynn_pos_reviews.csv")



wordcloud_Venetian_pos = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40, 
                          random_state=42,
                         ).generate(str(data['pos_review']))




print(wordcloud_Venetian_pos)
fig = plt.figure(1)
plt.imshow(wordcloud_Venetian_pos)
plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=4000)

#save_path = 'C:/Users/Nitin/Desktop/data_gathering'
#completeName = os.path.join(save_path, wordcloud1+".png") 
#file1 = open(completeName, "w")
wordcloud_Venetian_pos.to_file('C:/Users/Nitin/Desktop/data_gathering/wordcloud_Venetian_pos.png')