import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib3
import time
import random

url_1 = 'https://www.booking.com/reviews/us/hotel/wynn-las-vegas-boulevard.html?aid=304142;label=gen173nr-1FCAEoggJCAlhYSDNYBHIFdXNfbmqIAQGYATHCAQp3aW5kb3dzIDEwyAEM2AEB6AEB-AECkgIBeagCAw;sid=b88de736b1557b87baaeffc576661734;customer_type=total;hp_nav=0;old_page=0;order=featuredreviews;page='
url_2 = ';r_lang=en;rows=75&'
page_number = 1
data = []
neg_data = []
pos_data = []
while page_number <= 9:
    final_url = url_1 + str(page_number) + url_2
    res = requests.get(final_url)
    soup = bs(res.text, "html5lib")
    neg_reviews = soup.find_all('p', {'class': 'review_neg'})
    neg_review_list = [i.text.strip().replace('눉', '') for i in neg_reviews]  # negitive reviews

    pos_reviews = soup.find_all('p', {'class': 'review_pos'})
    pos_review_list = [i.text.strip().replace('눇', '') for i in pos_reviews]  # positive revews

    info = soup.find_all('span', {'itemprop': 'name'})
    info_list = []
    name_list = []
    nationality_list = []
    topic_list = []
    for i in range(len(info)):
        info_list.append(str(info[i].text))
    for i in range(len(info_list)):
        if i % 3 == 0:
            name_list.append(info_list[i])
        elif i % 3 == 1:
            nationality_list.append(info_list[i])
        elif i % 3 == 2:
            topic_list.append(info_list[i])  # name, nation, topic

    reviews_number = soup.find_all('div', {'class': 'review_item_user_review_count'})
    reviews_number_list = [i.text.strip() for i in reviews_number]  # reviews number

    scores = soup.find_all('span', {'class': 'review-score-badge'})
    scores_list = []
    for i in range(len(scores)):
        scores_list.append(scores[i].text.strip())
    scores_list.pop(0)  # scores

    review_date = soup.find_all('p', {'class': 'review_item_date'})
    review_date_list = [i.text.strip() for i in review_date]  # review date

    tags = soup.find_all('ul', {'class': 'review_item_info_tags'})
    tag_list = [i.text.strip().replace('\n\n\n', '') for i in tags]  # tags

    for x in range(len(name_list)):
        data.append([name_list[x], nationality_list[x], review_date_list[x], scores_list[x], topic_list[x], tag_list[x],
                     reviews_number_list[x]])

    for y in range(len(neg_review_list)):
        neg_data.append(neg_review_list[y])

    for z in range(len(pos_review_list)):
        pos_data.append(pos_review_list[z])

    time.sleep(random.randint(2, 4))
    page_number += 1

df_over=pd.DataFrame(data)
df_pos=pd.DataFrame(pos_data)
df_neg=pd.DataFrame(neg_data)

df_over.columns = ['Name','Nationality','Date','Score','Topic','Tags','History reviews']

df_over.to_csv(r'C:\Users\yuxia\Desktop\booking_data\wynn_overall_data.csv')
df_pos.to_csv(r'C:\Users\yuxia\Desktop\booking_data\wynn_pos_reviews.csv')
df_neg.to_csv(r'C:\Users\yuxia\Desktop\booking_data\wynn_neg_reviews.csv')