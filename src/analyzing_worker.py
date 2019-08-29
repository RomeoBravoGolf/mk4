import os
from rq import Queue
import redis
from rq import Worker
from redis import Redis

def work():
    redis_conn = Redis()
    parser = Worker(['analyzing'], connection=redis_conn)

    parser.work()

work()