from rq import Queue
from redis import Redis
from services import scraping_service
from services import analyzing_service
from config import constants
import time

class Scheduler:
    def __init__(self):
        redis_conn = Redis()
        self.scraping_q = Queue('scraping', connection=redis_conn)

    def scheduler_loop(self, url, time_interval, fmt):
        while True:
            self.scraping_q.enqueue(scraping_service.scrape, url, time_interval, fmt, job_timeout=-1)
            print("Added scraping job to the queue.")
            time.sleep(time_interval - constants.SCRAPER_UP_OFFSET)

    def run(self, url="https://www.youtube.com/watch?v=-1xif50QMr4", interval=60*5, fmt=94):
        self.scheduler_loop(url, interval, fmt)
