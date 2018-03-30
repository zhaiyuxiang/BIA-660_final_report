import requests, csv
from bs4 import BeautifulSoup
import unicodedata
from time import sleep
import pandas as pd

review_pos_list = []
review_neg_list = []
name_list = []
reviewer_nationality_list = []
review_date_list = []
tag_list = []
review_score_list = []
review_times_list = []
review_total_list = []

count = 1
# with open('suv_csv.csv', "a") as out_f:
#    writer = csv.writer(out_f)

base_url = "https://www.booking.com/reviews/us/hotel/the-venetian-resort-casino.html?aigF5qAID;sid=6c0b67bcb88b155b34d7f96d74c0049c;customer_type=total;hp_nav=0;old_page=0;order=featuredreviews;page="
end_url = ";r_lang=en;rows=75&amp;"
page_url = base_url + str(count) + end_url

while page_url != None:
    page_url = base_url + str(count) + end_url
    page = requests.get(page_url)
    count += 1
    print(count)
    if page.status_code != 200:
        page_url = None
    else:
        soup = BeautifulSoup(page.content, 'html.parser')

        all = soup.find_all("ul", {"class": "review_list"})
        for item in all:
            review_neg = item.find_all('p', attrs={'class': 'review_neg'})
            hotel_reviews_neg = [s.find('span', attrs={'itemprop': 'reviewBody'}).text.strip() for s in review_neg]
            review_neg_list.append(hotel_reviews_neg)

            review_pos = item.find_all('p', attrs={'class': 'review_pos'})
            hotel_reviews_pos = [s.find('span', attrs={'itemprop': 'reviewBody'}).text.strip() for s in review_pos]
            review_pos_list.append(hotel_reviews_pos)

            names = item.find_all('h4')
            publisher = [s.find('span', attrs={'itemprop': 'name'}).text.strip() for s in names]
            name_list.append(publisher)

            reviewer_countries = item.find_all('span', attrs={'class': 'reviewer_country'})
            nationality = [s.find('span', attrs={'itemprop': 'name'}).text.strip() for s in reviewer_countries]
            reviewer_nationality_list.append(nationality)

            review_date = item.find_all('p', attrs={'class': 'review_item_date'})
            date = [s.text.strip() for s in review_date]
            review_date_list.append(date)

            tags = item.find_all('ul', attrs={'class': 'review_item_info_tags'})
            tag = [s.text.strip() for s in tags]
            tag_list.append(tag)

            scores = item.find_all('span', attrs={'class': 'review-score-widget'})
            review_score = [s.find('span', attrs={'class': 'review-score-badge'}).text.strip() for s in scores]
            review_score_list.append(review_score)

            review_times = item.find_all('div', attrs={'class': 'review_item_user_review_count'})
            review_times = [s.text.strip() for s in review_times]
            review_times_list.append(review_times)

            review_total = item.find_all('a', attrs={'class': 'review_item_header_content'})
            reviews_total = [s.find('span', attrs={'itemprop': 'name'}).text.strip() for s in review_total]
            review_total_list.append(reviews_total)

def magic(dumy):
    new_dumy = []
    super_dumy = []
    for i in dumy:
        new_dumy.append(';'.join(i))
    super_dumy = ';'.join(new_dumy).split(';')
    return super_dumy

reviewer_nationality_list_new = magic(reviewer_nationality_list)
name_list_new=magic(name_list)
review_date_list_new=magic(review_date_list)
tag_list_new=magic(tag_list)
review_score_list_new=magic(review_score_list)
review_times_list_new=magic(review_times_list)
review_total_list_new=magic(review_total_list)
review_pos_list_new=magic(review_pos_list)
review_neg_list_new=magic(review_neg_list)

del(review_total_list_new[2929:2933])

import pandas as pd
dic={"name" : name_list_new,
     "nationality" : reviewer_nationality_list_new,
     "date": review_date_list_new,
     "tag": tag_list_new,
     "rating":review_score_list_new,
     "review_times":review_times_list_new,
     "Overall_review":review_total_list_new}

df=pd.DataFrame(dic)

df.to_csv("/Users/richard/Desktop/660D Web Analytics/Final_project/The_Venetian Resort-Hotel-Casino.csv")

dic2={"pos_review":review_pos_list_new}
dic3={"neg_review":review_neg_list_new}

df_pos_review=pd.DataFrame(dic2)
df_neg_review=pd.DataFrame(dic3)

df_pos_review.to_csv("/Users/richard/Desktop/660D Web Analytics/Final_project/The_Venetian_pos_review.csv")
df_neg_review.to_csv("/Users/richard/Desktop/660D Web Analytics/Final_project/The_Venetian__review.csv")