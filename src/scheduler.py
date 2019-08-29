from rq import Queue
from redis import Redis
from services import scraping_service
from services import analyzing_service
from services import reporting_service
from config import Constants
import datetime
import time

class Scheduler:
    def __init__(self):
        redis_conn = Redis()
        self.scraping_q = Queue('scraping', connection=redis_conn)
        self.reporting_q = Queue('reporting', connection=redis_conn)

    def scheduler_loop(self, url, time_interval, fmt, report_time):
        time_since_last_report = 0
        while True:
            if(time_since_last_report>report_time):
                self.reporting_q.enqueue(reporting_service.report(datetime.datetime.now()))
                time_since_last_report = 0

            self.scraping_q.enqueue(scraping_service.scrape, url, time_interval, fmt, job_timeout=-1)
            print("Added scraping job to the queue.")
            interval = time_interval - Constants.SCRAPER_UP_OFFSET
            time.sleep(interval)
            time_since_last_report += interval


    def run(self, url="https://www.youtube.com/watch?v=-1xif50QMr4", interval=60*5, fmt=94, report_time=24*60*60):
        self.scheduler_loop(url, interval, fmt, report_time)
