"""네이버 뉴스 기사 웹 크롤러 모듈"""

from bs4 import BeautifulSoup
import urllib.request
import re
import openpyxl

import os
import sys
import urllib.request
import datetime
import time
import json
from config import *


#출력 파일 명
OUTPUT_FILE_NAME = 'output.txt'
#긁어 올 URL
URL = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=001&aid=0010496075'



def get_request_url(url):

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id","") # naver app id 입력
    req.add_header("X-Naver-Client-Secret","") # naver app secret 입력
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(),url))
        return None

def getNaverSearchResult(sNode, search_text, page_start, display):

    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % sNode

    parameters = "?query=%s" % urllib.parse.quote(search_text)
    url = base + node + parameters

    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)

def getPostData(post, jsonResult):

    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title':title, 'descripton':description,
                       'org_link':org_link, 'link':org_link,
                       'pDate':pDate})
    return title


def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))

    return text

def clean_text(text):
    text = re.sub('[a-zA-Z]', '', text)
    text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', text)
    return text

def replace_text(text):
    text = text.replace("본문 내용","")
    text = text.replace("플레이어","")
    text = text.replace("▶놓치면 아쉬운 핫뉴스","")
    text = text.replace("▶뉴스가 보여요  연합뉴스 유튜브","")
    text = text.replace("▶네이버 홈에서 연합뉴스 채널 구독하기","")

    return text

if __name__ == "__main__":
    # open_output_file = open(OUTPUT_FILE_NAME, 'w')

    jsonResult = []

    # 'news', 'blog', 'cafearticle'

    sNode = 'news' #원하는 검색 종류
    search_text = "미세먼지" #원하는 검색어 입력
    display_count = 100

    jsonSearch = getNaverSearchResult(sNode, search_text,1,display_count)

    while((jsonSearch != None) and (jsonSearch['display'] != 0)):
        for post in jsonSearch['items']:
            getPostData(post,jsonResult)


        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)

    with open('%s_naver_%s.json' % (search_text,sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False)
        outfile.write(retJson)

        print('%s_naver_%s.json SAVED' % (search_text, sNode))


    wb = openpyxl.load_workbook('test.xlsx')
    ws = wb.active      #워크 시트를 얻는다

    text = get_text(URL)
    text = clean_text(text)
    text = replace_text(text)

    ws['C1'] = text
    wb.save('test.xlsx')

    print(text)

