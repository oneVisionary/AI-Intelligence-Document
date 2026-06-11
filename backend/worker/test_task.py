from worker.celery_app import celery_app


@celery_app.task
def add(x, y):
    print(f"Adding {x} + {y}")

    return x + y
