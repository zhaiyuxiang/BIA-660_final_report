"""
Reference: https://www.kaggle.com/adiljadoon/word-cloud-with-python/notebook
"""

import numpy as np # linear algebra
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
#matplotlib inline

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

data_Venetian_allreview = pd.read_csv("C:/Users/Nitin/PycharmProjects/BIA660D_Group_6_Project/data_gathering/The_Venetian Resort-Hotel-Casino.csv")
data_Caesars_allreview = pd.read_csv("C:/Users/Nitin/PycharmProjects/BIA660D_Group_6_Project/data_gathering/Caesar_palace_overall.csv")
data_Wynn_allreview = pd.read_csv("C:/Users/Nitin/PycharmProjects/BIA660D_Group_6_Project/data_gathering/wynn_overall_data.csv")



wordcloud_Venetian_allreview = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40,
                          random_state=42,
                         ).generate(str(data_Venetian_allreview['Overall_review']))

wordcloud_Caesars_allreview = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40,
                          random_state=42,
                         ).generate(str(data_Caesars_allreview['Overall_review']))

wordcloud_Wynn_allreview = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40,
                          random_state=42,
                         ).generate(str(data_Wynn_allreview['Topic']))




print(wordcloud_Venetian_allreview)
print(wordcloud_Caesars_allreview)
print(wordcloud_Wynn_allreview)
fig = plt.figure(1)
plt.imshow(wordcloud_Venetian_allreview)
plt.imshow(wordcloud_Caesars_allreview)
plt.imshow(wordcloud_Wynn_allreview)

plt.axis('off')
plt.show()
fig.savefig("word1.png", dpi=4000)


wordcloud_Venetian_allreview.to_file('C:/Users/Nitin/Desktop/data_gathering/wc_Venetian_allreview.png')
wordcloud_Caesars_allreview.to_file('C:/Users/Nitin/Desktop/data_gathering/wc_Caesars_allreview.png')
wordcloud_Wynn_allreview.to_file('C:/Users/Nitin/Desktop/data_gathering/wc_Wynn_allreview.png')