from rq import Queue
from redis import Redis
from services import scraping_service
from services import analyzing_service
import time

class Scheduler:
    def __init__(self):
        redis_conn = Redis()
        self.scraping_q = Queue('scraping', connection=redis_conn)

    def scheduler_loop(self, url, time_interval):
        while True:
            self.scraping_q.enqueue(scraping_service.scrape, url, time_interval)
            print("Added scraping job to the queue.")
            time.sleep(time_interval)

    def run(self, url, interval):
        self.scheduler_loop(url, interval)
