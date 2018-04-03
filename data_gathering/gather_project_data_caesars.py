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