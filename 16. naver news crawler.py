import os
import sys
import urllib.request
import datetime
import time
import json
from config import *

def get_request_url(url):

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id","Ch0vdY0HM6SPOidkt02i") # naver app id 입력
    req.add_header("X-Naver-Client-Secret","ANmaZHqA8m") # naver app secret 입력
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
    return

def main():

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

if __name__ == '__main__':
    main()