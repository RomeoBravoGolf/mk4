from rq import Queue
from redis import Redis
from services import scraping_service
from services import analyzing_service
import time

def schedule_loop(url, time_interval):
    redis_conn = Redis()
    scraping_q = Queue('scraping', connection=redis_conn)

    while True:
        scraping_q.enqueue(scraping_service.scrape, url, time_interval)
        print("Added scraping job to the queue.")
        time.sleep(time_interval)

schedule_loop("https://www.youtube.com/watch?v=-1xif50QMr4", 10)