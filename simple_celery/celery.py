from celery import Celery

app = Celery('simple_celery',
             broker='amqp://guest@localhost//',
             backend='amqp://guest@localhost//',
             include=['simple_celery.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()