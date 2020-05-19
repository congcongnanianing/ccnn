from celery import shared_task
import time


@shared_task
def add(a, b):
    time.sleep(10)
    return a + b


@shared_task
def multi(a, b):
    time.sleep(30)
    return a * b


@shared_task
def send_msg(m, n):
    return m ** n
