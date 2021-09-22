import wget
import requests
from bs4 import BeautifulSoup
import zipfile,os
import gzip

def zip_extract(file_path,path):
    zf = zipfile.ZipFile(file_path, 'r')
    zf.extractall(path)

def get_daily_futures():
    r = requests.get("https://www.taifex.com.tw/cht/3/dlFutPrevious30DaysSpreadOrdersReport") # futures
    soup = BeautifulSoup(r.text,'lxml')
    res = soup.select('#printhere table:nth-child(4) > tr > td:nth-child(4)')
    # f = open('t.txt','w',encoding='utf8')

    for ele in res:
        url = ele.find('input')['onclick'].split('\'')[1].split('\'')[0]
        url = url.replace('_B','')
        wget.download(url, url.split('/')[-1])
        zip_extract(url.split('/')[-1],"DailyFuturesCSV")
        os.remove(url.split('/')[-1])
        # f.write(str(url)+'\n')

def get_daily_options():
    r = requests.get("https://www.taifex.com.tw/cht/3/dlOptPrevious30DaysSalesData") # options
    soup = BeautifulSoup(r.text,'lxml')
    res = soup.select('#printhere table:nth-child(4) > tr > td:nth-child(4)')
    # f = open('t.txt','w',encoding='utf8')

    for ele in res:
        url = ele.find('input')['onclick'].split('\'')[1].split('\'')[0]
        url = url.replace('_B','')
        wget.download(url, url.split('/')[-1])
        zip_extract(url.split('/')[-1],"DailyOptionsCSV")
        os.remove(url.split('/')[-1])
        # f.write(str(url)+'\n')

if __name__ == '__main__':
    get_daily_options()
    get_daily_futures()
