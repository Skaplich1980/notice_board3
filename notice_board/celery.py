import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notice_board.settings')


# передача задачи в celery для выполнения асинхронно, потому что данная рассылка может замедлять работу
app = Celery('notice_board')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Europe/Minsk'
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'send_mail_monday_8am': {
        'task': 'board.tasks.task_mail_week',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'), # рассылка в 8 утра по понедельникам
    },
}
