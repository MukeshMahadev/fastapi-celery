This app is used for supporting asynchrnous operations like long running AI/ML tasks.

 

Steps to Run 
1. Download docker redis
2. Start the app
   `python main.py`
3. Start the celery worker
    ` celery -A celery_worker worker --pool=solo --loglevel=info`
4. Check the API reference at `/docs` endpoint.
5. Make a request to add a task and check the status.