from celery import Celery
from celery.schedules import crontab
from .config import WorkerSettings
from parser_1 import parse_better_funding_rate
from db.dal.funding import FundingDAL
from db.client import session_maker

settings = WorkerSettings()
app = Celery(
    "tasks", backend=settings.celery_result_backend, broker=settings.celery_broker_url
)

app.conf.beat_schedule = {
    "hello": {
        "task": "app.add",
        "schedule": crontab(minute="*/1"),
    },
}
app.conf.timezone = "Europe/Moscow"


@app.task(name="app.add")
def add():
    funding_list = parse_better_funding_rate()
    for i in funding_list:
        FundingDAL(session_maker).get_or_create(i, symbol=i["symbol"])
