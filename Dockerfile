FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /napptilus_iati

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /napptilus_iati

RUN apt-get update && apt-get install cron -y && apt install systemctl

RUN python3 manage.py migrate

RUN python3 manage.py loaddata apps/products/fixtures/initial_data.json

RUN python3 manage.py crontab add

CMD ["bash", "init.sh"]