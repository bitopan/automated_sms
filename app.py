import sys
from redis import Redis
#from rq import Queue, Connection, Worker
from rq import Queue, Connection, Worker
from rq_scheduler import Scheduler

from main import send_msg, get_employees

q = Queue(connection=Redis())

#scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue


def make_queue():
    users = get_employees()
    for employee in users:
        print("Adding " + employee[0] + " to Message Queue")
        #q.enqueue(send_msg, employee[0], employee[1], employee[2])
        #scheduler.enqueue_at(datetime.datetime.utcnow() + timedelta(minutes=1), send_msg) # Date time should be in UTC

    # with Connection():
    # 	qs = sys.argv[1:] or ['default']

    # 	w = Worker(qs)
    # 	w.work()

if __name__ == '__main__':
    make_queue()
