from scheduler import Scheduler
import sys

if __name__ == '__main__':
    scheduler = Scheduler()
    args = sys.argv
    scheduler.run(args[1], args[2], args[3])
