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

import random
import os
import requests
import selenium
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

url = """https://www.booking.com/reviews/us/hotel/harrah-s-caesars-palace.html?label=gen173nr-1DCA0o7AFCF2hhcnJhaC1zLWNhZXNhcnMtcGFsYWNlSDNYBHIFdXNfbmqIAQGYATHCAQp3aW5kb3dzIDEwyAEM2AED6AEB-AEIkgIBeagCAw;sid=1af5ab0c2b606d0e4a71070aff10463c;customer_type=total;hp_nav=0;old_page=0;order=featuredreviews;page=1;r_lang=en;rows=75&"""

driver = webdriver.Chrome(executable_path=r'C:\Users\Nitin\Desktop\Desktop FOlder\chromedriver.exe')
# print(BASE_DIR + '/web_analytics/chromedriver.exe')
# driver = webdriver.Chrome(executable_path=BASE_DIR + '/web_analytics/chromedriver')

driver.get(url)

"""
Scraping Data from the site
"""

rating_list = []
overall_list = []
negative_list = []
positive_list = []
tags_list = []
country_list = []
date_list = []
RESULT = []
POSITIVE = []
NEGATIVE = []

page = 0
while page < 20:
    count = 1

    while count < 76:
        #  Rating by reviewer
        rating_reviews = driver.find_elements_by_xpath(
            '//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/div[1]/div[1]'.format(count))
        rating = [x.text.strip() for x in rating_reviews]
        rating_list.append(rating)

        # overall of Review
        overall_reviews = driver.find_elements_by_xpath(
            '//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/div[1]/div[2]'.format(count))
        overall = [x.text for x in overall_reviews]
        overall_list.append(overall)

        # Negative Reviews
        negative_reviews = driver.find_elements_by_xpath(
            '//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/div[2]/p[1]'.format(count))
        negative = [x.text for x in negative_reviews]
        negative_list.append(negative)

        # Positive Reviews
        positive_reviews = driver.find_elements_by_xpath(
            '//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/div[2]/p[2]'.format(count))
        positive = [x.text for x in positive_reviews]
        positive_list.append(positive)

        # Tags for Reviewers
        tags_reviews = driver.find_elements_by_xpath(
            '//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/ul'.format(count))
        tags = [x.text for x in tags_reviews]
        tags_list.append(tags)

        # Country of Reviewers
        country_reviews = driver.find_elements_by_xpath(
            '//*[@id="review_list_page_container"]/ul/li[{}]/div[3]/span/span[2]'.format(count))
        country = [x.text for x in country_reviews]
        country_list.append(country)

        # Date of Review
        date_reviews = driver.find_elements_by_xpath('//*[@id="review_list_page_container"]/ul/li[{}]/p'.format(count))
        date = [x.text.strip() for x in date_reviews]
        date_list.append(date)

        count = count + 1

    # try:
    #    RESULT.append(dict(zip(['overall', 'date', 'nationality', 'rating', 'tags'],
    #                          [overall_reviews[0].text, negative_reviews[0].text, country_reviews[0].text,
    #                          rating_reviews[0].text, tags_reviews[0].text])))
    # POSITIVE.append((dict(zip(['positive'], [positive_reviews[0].text]))))
    # NEGATIVE.append((dict(zip(['negative'], [negative_reviews[0].text]))))

    # except:
    #   pass

    # RESULT.append([country, rating, tags, negative, positive])

    try:
        next_page = driver.find_element_by_xpath('//*[@id="review_next_page_link"]').click()
    except:
        break

    # Wait for browsing
    time.sleep(random.randint(1, 3))
    page += 1

driver.close()


"""
Moving Data to csv file using Pandas
"""


def magic(dumy):
    new_dumy = []
    super_dumy = []
    for i in dumy:
        new_dumy.append(';'.join(i))
    super_dumy = ';'.join(new_dumy).split(';')
    return super_dumy


country_reviews_list_new = magic(country_list)
# name_list_new=magic(name_list)
date_reviews_list_new = magic(date_list)
tags_reviews_list_new = magic(tags_list)
rating_reviews_list_new = magic(rating_list)
# review_times_list_new=magic(review_times_list)
overall_reviews_list_new = magic(overall_list)
overall_reviews_list_new.pop()
positive_reviews_list_new = magic(positive_list)
negative_reviews_list_new = magic(negative_list)

print(len(overall_reviews_list_new), len(country_reviews_list_new), len(date_reviews_list_new),
      len(tags_reviews_list_new))
print(len(positive_reviews_list_new), len(negative_reviews_list_new))

import pandas as pd

dic2 = {"pos_review": positive_reviews_list_new}
dic3 = {"neg_review": negative_reviews_list_new}

df_pos_review = pd.DataFrame(dic2)
df_neg_review = pd.DataFrame(dic3)

df_pos_review.to_csv("C:/Users/Nitin/Desktop/BIA660D/Project- Hotel Reviews/Caesar_palace_pos_review.csv")
df_neg_review.to_csv("C:/Users/Nitin/Desktop/BIA660D/Project- Hotel Reviews/Caesar_palace_neg_review.csv")

dic = {"nationality": country_reviews_list_new,
       "date": date_reviews_list_new,
       "tag": tags_reviews_list_new,
       "rating": rating_reviews_list_new,
       "Overall_review": overall_reviews_list_new}

# df=pd.DataFrame(dic)

df = pd.DataFrame(dic)
df.to_csv("C:/Users/Nitin/Desktop/BIA660D/Project- Hotel Reviews/Caesar_palace_overall.csv")