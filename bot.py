# discord 라이브러리 사용 선언
import discord
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--start-fullscreen')

driver = webdriver.Chrome("chromedriver",  options=options)

def tierfinder(word):
    if word.find('tier/1.svg') != -1:
        return "브론즈 5"
    elif word.find('tier/2.svg') != -1:
        return "브론즈 4"
    elif word.find('tier/3.svg') != -1:
        return "브론즈 3"
    elif word.find('tier/4.svg') != -1:
        return "브론즈 2"
    elif word.find('tier/5.svg') != -1:
        return "브론즈 1"
    elif word.find('tier/6.svg') != -1:
        return "실버 5"
    elif word.find('tier/7.svg') != -1:
        return "실버 4"
    elif word.find('tier/8.svg') != -1:
        return "실버 3"
    elif word.find('tier/9.svg') != -1:
        return "실버 2"
    elif word.find('tier/10.svg') != -1:
        return "실버 1"
    elif word.find('tier/11.svg') != -1:
        return "골드 5"
    elif word.find('tier/12.svg') != -1:
        return "골드 4"
    elif word.find('tier/13.svg') != -1:
        return "골드 3"
    elif word.find('tier/14.svg') != -1:
        return "골드 2"
    elif word.find('tier/15.svg') != -1:
        return "골드 1"
    elif word.find('tier/16.svg') != -1:
        return "플래티넘 5"
    elif word.find('tier/17.svg') != -1:
        return "플래티넘 4"
    elif word.find('tier/18.svg') != -1:
        return "플래티넘 3"
    elif word.find('tier/19.svg') != -1:
        return "플래티넘 2"
    elif word.find('tier/20.svg') != -1:
        return "플래티넘 1"
    elif word.find('tier/21.svg') != -1:
        return "다이아몬드 5"
    elif word.find('tier/22.svg') != -1:
        return "다이아몬드 4"
    elif word.find('tier/23.svg') != -1:
        return "다이아몬드 3"
    elif word.find('tier/24.svg') != -1:
        return "다이아몬드 2"
    elif word.find('tier/25.svg') != -1:
        return "다이아몬드 1"
    elif word.find('tier/26.svg') != -1:
        return "루비 5"
    elif word.find('tier/27.svg') != -1:
        return "루비 4"
    elif word.find('tier/28.svg') != -1:
        return "루비 3"
    elif word.find('tier/29.svg') != -1:
        return "루비 2"
    elif word.find('tier/30.svg') != -1:
        return "루비 1"
    elif word.find('tier/31.svg') != -1:
        return "마스터"
    else:
        return "언랭크"


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("!도움말")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None
        
        # message.content = message의 내용
        if message.content == "!공지":
            # 현재 채널을 받아옴
            channel = message.channel
            await channel.send(file=discord.File("gongji.txt"))
            return None
        if message.content == "!도움말" or message.content == "!help" or message.content == "!도움" or message.content == "!명령어":
            channel = message.channel
            await channel.send("!공지 : 코딩/프로그래밍 초보자방 [입장코드:해시태그]\n!백준 (유저네임) : 백준에서 유저의 정보를 불러옵니다")
            return None
        if message.content.startswith("!백준"):
            channel = message.channel
            usrname = message.content.split(" ")
            url = f"https://www.acmicpc.net/user/{usrname[1]}"
            url2 = f"https://solved.ac/profile/{usrname[1]}"
            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            tierimg = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(1) > div > h1 > img")
            tier = tierfinder(str(tierimg))
            rank = soup.select_one("#statics > tbody > tr:nth-child(1) > td")
            solved = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(1) > div.panel-body")
            wrong = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div.panel-body")
            tier1 = str(tierimg).lstrip('<img class="solvedac-tier" src="')
            tier2 = tier1.rstrip('"/>')
            f = open("rank.txt", "w", encoding = "utf-8")
            f.write(f"티어:{tier}\n랭크:{rank.get_text()}\n푼 문제:{solved.get_text()}\n틀린 문제:{wrong.get_text()}")
            f.close()
            await channel.send(file=discord.File("rank.txt")) 
            driver.get(tier2)
            driver.save_screenshot("tier.png")
            await channel.send(file=discord.File("tier.png"))
            driver.get(url2)
            driver.execute_script("window.scrollTo(0, 0)")  
            driver.save_screenshot("solvedac1.png")
            await channel.send(file=discord.File("solvedac1.png"))
            driver.execute_script("window.scrollTo(0, 500)")  

            


    


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("ODY3MDQ0NTU4OTU2Nzg5Nzgw.YPbYKw.qiIpTR_Hznb4m-czbdWzuuWSGaY")