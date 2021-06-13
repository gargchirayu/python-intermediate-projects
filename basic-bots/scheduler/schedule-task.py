import os
import time
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler


def task_to_automate():
    print("Scheduled task running")


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # works in 3 different modes : interval, start/end time, one-off
    scheduler.add_job(task_to_automate, 'interval', seconds=10)
    scheduler.start()
    # to provide functionality of exiting scheduler
    print("Press Ctrl+{0} to exit".format('Break' if os.name == 'nt' else 'C'))

    try:
        # to keep main thread active
        while True:
            time.sleep(2)

    except (KeyboardInterrupt, SystemExit):
        # not needed, but better to do if possible
        scheduler.shutdown()
