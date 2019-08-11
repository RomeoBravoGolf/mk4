import os
import datetime
import subprocess
from rq import Queue
import redis
from redis import Redis
from services import analyzing_service

def scrape(url, interval, fmt):
    filename = "../out/"+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".ts"
    os.system("pwd")
    p = subprocess.Popen(["./services/scraper.sh", url, str(interval), filename, str(fmt)])
    p.wait()

    redis_conn = Redis()
    analyzing_q = Queue('analyzing', connection=redis_conn)
    analyzing_q.enqueue(analyzing_service.analyze, filename)
