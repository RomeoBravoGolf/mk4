from scheduler import Scheduler
import sys

if __name__ == '__main__':
    scheduler = Scheduler()
    args = sys.argv
    args[0:1] = []
    scheduler.run(*args)
