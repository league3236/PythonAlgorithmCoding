from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import datetime
import os

chrome_options = Options()

chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")



driver = webdriver.Chrome(executable_path='/home/slackchat/crawlexe/data/chromedriver', chrome_options=chrome_options)

driver.implicitly_wait(2)
driver.get('http://ldccteam.lotte.net/SiteDirectory/BigData/Lists/Calendar/calendar.aspx')
driver.find_element_by_id('UserID').send_keys('내id')
driver.find_element_by_id('UserPass').send_keys('내 ')
driver.find_element_by_xpath('//*[@id="login"]').click()

driver.implicitly_wait(2)
driver.get('http://ldccteam.lotte.net/SiteDirectory/BigData/Lists/Calendar/calendar.aspx')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

calendars = soup.findAll("div", {"class": "ms-acal-rootdiv"})

href_list = []
for calendar in calendars:
    for link in calendar.findAll("a"):
        href = link["href"]
        if 'SiteDirectory' in href:
            href_list.append(href)

pre_domain = 'http://ldccteam.lotte.net'

now = datetime.datetime.now()


title_list = ''
pre_curl = 'curl -X POST --data-urlencode "payload={\"channel\": \"#jenkins\", \"username\": \"dailybot\", \"text\": \"'
post_curl = '\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/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'

for post_domain in href_list:
    web_url = pre_domain+post_domain
    driver.implicitly_wait(2)
    driver.get(web_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find("table", {"class": "ms-formtable"})
    soup = soup.findAll("td",{"class": "ms-formbody"})

    title = soup[0].text.strip()
    start_time = soup[2].text.strip()
    end_time = soup[3].text.strip()

    now_time = now.strftime("%m-%d")

    if now_time in start_time+end_time:
        title_list = title_list+title+'\n'

curl = pre_curl+title_list+post_curl
os.system(curl)





#    for td in soup.findAll("td",{"class": "ms-formbody"}):
#        print(td.text.strip())
#    break
