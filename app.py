import sys
from redis import Redis
from rq import Queue, Connection
from rq_scheduler import Scheduler

from main import send_msg, get_employees

q = Queue(connection=Redis())

def make_queue():
    users = get_employees()
    for employee in users:
        print("Adding " + employee[0] + " to Message Queue")
        q.enqueue(send_msg, employee[0], employee[1], employee[2])

if __name__ == '__main__':
    make_queue()
