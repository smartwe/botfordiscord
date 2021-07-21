import time
import schedule
import os

def f():
    os.system("python bot.py")
 
 
schedule.every(30).minutes.do(f)
 
#실제 실행하게 하는 코드
while True:
    schedule.run_pending()
    time.sleep(1)