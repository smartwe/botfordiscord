# discord 라이브러리 사용 선언
import discord
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
import os
from selenium.webdriver.common.keys import Keys
import os

token = os.environ['BOT_TOKEN']
os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ")
os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
os.system("chmod 777 chromedriver")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--start-fullscreen')

driver = webdriver.Chrome("./chromedriver",  options=options)
driver.set_window_size(1920, 1080)

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

 
client = discord.Client()
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("!도움말")
    await client.change_presence(status=discord.Status.online, activity=game)
 
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'test!!!!')
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
        await channel.send('!공지 : 코딩/프로그래밍 초보자방 [입장코드:해시태그]\n!백준 (유저네임) : 백준에서 유저의 정보를 불러옵니다\n!Python==>(소스코드)==>(입력받을 것): python 소스코드를 컴파일\n!JAVA(위와 동일)!C++(위와 동일)\n')
        return None
    if message.content.startswith("!백준 "):
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
    if message.content.startswith("!C++"):
        driver.set_window_size(1920, 1080)
        channel = message.channel
        code = message.content.split("==>")
        compiler = "https://tio.run/#cpp-gcc"
        driver.get(compiler)
        code[2] = ""
        driver.find_element_by_id("code").send_keys(code[1])
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/h3[5]/label").click()
        driver.find_element_by_id("input").send_keys(code[2])
        driver.find_element_by_id("run").click()
        time.sleep(2)
        driver.save_screenshot("tio.png")
        await channel.send(file=discord.File("tio.png"))

    if message.content.startswith("!JAVA"):
        driver.set_window_size(1920, 1080)
        channel = message.channel
        code = message.content.split("==>")
        compiler = "https://tio.run/#java-jdk"
        driver.get(compiler)
        code[2] = ""
        driver.find_element_by_id("code").send_keys(code[1])
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/h3[5]/label").click()
        driver.find_element_by_id("input").send_keys(code[2])
        driver.find_element_by_id("run").click()
        time.sleep(2)
        driver.save_screenshot("tio.png")
        await channel.send(file=discord.File("tio.png"))     
    if message.content.startswith("!Python") or message.content.startswith("!PY"):
        driver.set_window_size(1920, 1080)
        channel = message.channel
        code = message.content.split("==>")
        compiler = "https://tio.run/#python3-pypy"
        driver.get(compiler)
        code[2] = ""
        driver.find_element_by_id("code").send_keys(code[1])
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/h3[5]/label").click()
        driver.find_element_by_id("input").send_keys(code[2])
        driver.find_element_by_id("run").click()
        time.sleep(2)
        driver.save_screenshot("tio.png")
        await channel.send(file=discord.File("tio.png"))     
    if message.content.startswith("!백준이미지 ") or message.content.startswith("!백준임지 "):
        channel = message.channel
        usrname = message.content.split(" ")
        driver.get(f"http://mazassumnida.wtf/api/generate_badge?boj={usrname[1]}")
        driver.set_window_size(350, 170)
        time.sleep(3)
        driver.save_screenshot("bojimg.png")
        await channel.send(file=discord.File("bojimg.png"))
    if message.content.startswith("!백준정답"):
        channel = message.channel
        question = message.content.split(" ")
        await channel.send(file=discord.File(f"boj/BOJ/{question[1]}.cpp"))
    if message.content == "!오늘의 문제" or message.content == "!오늘의 문제 보기":
        channel = message.channel
        driver.get("https://github.com/tony9402/baekjoon/blob/main/picked.md")
        driver.save_screenshot("todayproblem.png")
        await channel.send(file=discord.File(f"todayproblem.png"))


        


client.run(BOT_TOKEN)