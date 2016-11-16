from celery import Celery

app = Celery('datasite', backend='rpc://',  broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y

result = add.delay(4, 4)
print(result.backend)
a = result.ready()
print(a)
a = result.get(timeout=100)
print(a)
