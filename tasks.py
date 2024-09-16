from celery import Celery

app = Celery('tasks')

# using redis as the result backend and rabbitmq as the broker
# app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')

# celery configurations
# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Europe/Oslo',
#     enable_utc=True,
# )

# Telling your celery app t use a configuration module
app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    print(f"Adding {x} and {y}")
    return x+y
