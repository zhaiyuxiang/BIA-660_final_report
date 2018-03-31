import random
import requests
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = """https://www.booking.com/reviews/us/hotel/harrah-s-caesars-palace.html?label=gen173nr-1DCA0o7AFCF2hhcnJhaC1zLWNhZXNhcnMtcGFsYWNlSDNYBHIFdXNfbmqIAQGYATHCAQp3aW5kb3dzIDEwyAEM2AED6AEB-AEIkgIBeagCAw;sid=1af5ab0c2b606d0e4a71070aff10463c;customer_type=total;hp_nav=0;old_page=0;order=featuredreviews;page=1;r_lang=en;rows=75&"""

driver = webdriver.Chrome(executable_path=r'C:\Users\Nitin\Desktop\Desktop FOlder\chromedriver.exe')

driver.get(url)

"""
Scraping Data from the site

"""
page = 0
while (page < 21):
    count = 1
    while (count < 76):

        # Rating
        rating_reviews = driver.find_elements_by_xpath(
            '//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/div[1]/div[1]'.format(count))
        rating = [x.text for x in rating_reviews]
        if not rating:
            break;
            # Subject Reviews
        subject_reviews = driver.find_elements_by_xpath('//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/div[1]/div[2]'.format(count))
        subject = [x.text for x in subject_reviews]

        # Negative Reviews
        negative_reviews = driver.find_elements_by_xpath('//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/div[2]/p[1]'.format(count))
        negative = [x.text for x in negative_reviews]

        # Positive Reviews
        positive_reviews = driver.find_elements_by_xpath('//*[@id="review_list_page_container"]/ul/li[{}]/div[4]/div/div[2]/p[2]'.format(count))
        positive = [x.text for x in positive_reviews]

        count = count + 1

        # Print the scraped data

        print("RATING:", rating)
        print("HEADER:", subject)
        print("NEGATIVE REVIEW:", negative)
        print("POSITIVE REVIEW:", positive)
        print("***************************")

    next_page = driver.find_element_by_xpath('//*[@id="review_next_page_link"]').click()

    # Wait for browsing
    time.sleep(random.randint(1, 3))
    print("Next")
    page += 1;