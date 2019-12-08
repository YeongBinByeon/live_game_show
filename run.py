# 모듈 가져오기
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
from live_stream import live_stream

from flask import Flask

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

main_url = 'https://www.youtube.com/gaming/games'
live_list = []

#드라이버 로드
driver = wd.Chrome(executable_path='C:\code_folder\chrome_driver\chromedriver.exe')

#사이트 접속 (get)
driver.get(main_url)

gameCardList = []
yPos = 0
for i in range(1,21):
    time.sleep(1.5)
    yPos = yPos + (19000/20)
    driver.execute_script("window.scrollTo(0, %s);" % yPos)

gameCardList = driver.find_elements_by_tag_name('ytd-game-card-renderer')


for card in gameCardList:
    #print (card.get_attribute('innerHTML'))
    print (len(card.text.split('\n')))
    if len(card.text.split('\n')) == 2:
        name, viewerCount = card.text.split('\n')
    else:
        name = card.text
        viewerCount = "시청 인원 없음"
    imgLink = card.find_element_by_id('img').get_attribute('src')
    channelLink = card.find_element_by_tag_name('a').get_attribute('href')
    print ('-'*100)
    print(name + viewerCount)
    print (channelLink ) #그냥은 해당 게임명 채널 정보 출력된다. 옆 결과에서 live만 붙이면 실시간 방송 나옴.
    print (imgLink )
    obj = live_stream( 
            name,
            viewerCount,
            channelLink,
            imgLink
        )
    live_list.append(obj)
    #print (card.text)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')
    #return render_template('index.html', video1=defaultUrl + VIDEO_ID_LIST[0], video2=defaultUrl + VIDEO_ID_LIST[1], channelLink = defaultChannelUrl + CHANNEL_ID, title = channelName, thumbnails=imgUrl, subCount=subscriberCount, vidCount= videoCount)

app.run()