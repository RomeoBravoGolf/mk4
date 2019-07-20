from rq import Queue
from redis import Redis

from workers import analyzing_worker
from workers import scraping_worker
from services import scraping_service
from services import analyzing_service

import time


def schedule_loop(url, time_interval):
    redis_conn = Redis()
    scraping_q = Queue('scraping', connection=redis_conn)

    analyzing_worker.work()
    scraping_worker.work()

    while True:
        scraping_q.enqueue(scraping_service.scrape, url, time_interval)
        print("Added scraping job to the queue.")
        for i in range(1, time_interval):
            time.sleep(1)

schedule_loop("asdf", 10)