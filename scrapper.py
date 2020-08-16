from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

city = ["london", 'glasgow', 'birmingham', 'manchester',\
        'liverpool', 'oxford', 'cambridge', 'reading', 'bristol',\
        'cardiff', 'newcastle', 'edinburgh', 'southampton', 'norwich']

final_data = pd.DataFrame(columns=['title', 'company'])

driver.maximize_window()
for url in city:
    url = "https://www.indeed.co.uk/jobs?l="+url+"&q="
    flag = True
    while flag:        
        driver.get(url)
        cards = driver.find_elements_by_xpath('//*[@class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')

        for x in cards:
            title = x.find_element_by_class_name('jobtitle').get_attribute('title').lower()
            company = x.find_element_by_class_name('company').text.lower()
            final_data = final_data.append({"title": title, "company": company}, ignore_index=True)

        xpath = '//*[@id="resultsCol"]/nav/div/ul/li/a[@aria-label="Next"]'
        nxt = driver.find_elements_by_xpath(xpath)
        if len(nxt) > 0:
            url = nxt[0].get_attribute("href")
        else:
            flag = False

final_data = pd.DataFrame.drop_duplicates(final_data)
final_data.to_csv('data/indeed.csv', index=False)

driver.quit()