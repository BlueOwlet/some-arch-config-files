import multiprocessing

command='/var/www/new_ia/venv/bin/gunicorn'
pythonpath='/var/www/new_ia/venv'
bind='localhost:8000'
workers=multiprocessing.cpu_count()*2+1
timeout=60
