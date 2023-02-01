FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /napptilus_iati

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /napptilus_iati

CMD ["bash", "init.sh"]