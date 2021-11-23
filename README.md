# dj_celery
Integrated django celery to perform scheduled task

### Using environment variable.
Environment varibale keeps the secret keys and credentials like email address or password safe in production.

### Installing celery
```
pip install celery
```
#### Run Celery worker
```
celery -A dj_celery_pro.celery worker --pool=solo -l info
```
#### Run django-celery-beat
```
celery -A dj_celery_pro beat -l info
```