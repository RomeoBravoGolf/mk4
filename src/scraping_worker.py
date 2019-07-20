import os

import redis
from rq import Worker
from redis import Redis

def work():
    redis_conn = Redis()

    parser = Worker(['scraping'], connection=redis_conn, name='scraper')

    parser.work()

work()